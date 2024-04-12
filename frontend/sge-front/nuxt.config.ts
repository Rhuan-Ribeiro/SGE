// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue',
    '@sidebase/nuxt-auth'
  ],
  primevue: {
    components: {
      include: ['Button']
    }
  },
  css: [
    'primeicons/primeicons.css', //css dos ícones do primevue
    'primevue/resources/themes/aura-light-green/theme.css', // css tema dos componentes primevue
    '~/assets/style/global-project.sass', //variáveis css global customizado para toda a aplicação
    '~/assets/style/global-variables.sass', //css global customizado para toda a aplicação
  ],
  auth: {
    baseURL: 'http://localhost:8000',
    provider: {
      type: 'local', // local vai manter o token até acontecer o logout, assim como o Webtoken
      // type: 'refresh', // refresh vai atualiar o token de acesso, assim como o JWT
      endpoints: {
        signIn: { path: '/token/login/', method: 'POST' }, // rota de login
        signOut: { path: '/token/logout/', method: 'POST' }, // rota de logout
        signUp: { path: '', method: 'get' }, // rota de cadastro
        getSession: { path: '/users/', method: 'get' }, // rota autenticada para verificação se foi autenticado c/ sucesso
        // refresh: {}, // rota para renovar o token (somente no type refreh)
      },
      token: {
        signInResponseTokenPointer: '/auth_token', // indica o local do Token Acess na response do Backend
        //maxAgeInSeconds: 600, // validade do token acess
        type: 'Token'
      },
      // refreshToken: { signInResponseRefreshTokenPointer: '', // Local do Token Refresh
      // maxAgeInSeconds: 600, // validade do token refresh
      // },
      pages: {
        login: '/' // endereço (rota) da página de login
      }
    }
  }
})
