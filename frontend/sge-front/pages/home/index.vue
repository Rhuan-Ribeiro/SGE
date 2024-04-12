<script setup lang="ts">
    const { signOut } = useAuth();

    definePageMeta({
        middleware: 'auth' // essa tela será privada
    })

    const logout = () => {
        console.log("trying to logout");
        signOut({redirect: false}).then(()=>{
            console.log("sucessfully logged out!");
            navigateTo('/'); // redireciona para a página de login
        })
        // se o "then" da promise falhou, então esse bloco que será executado         
        .catch((e)=>{
            console.log("Error when trying to logout:", e);
        });
    }

</script>

<template>
    <div>
        <h1>Tela Home</h1>
        <button @click="logout" class="customButton">SAIR</button>
    </div>
</template>