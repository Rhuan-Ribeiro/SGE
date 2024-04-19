from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
# from django.core.exceptions import PermissionDenied
from django.db.models import Q


# Permite que apenas coordenadores façam POST/PUT/DELETE
# Estamos sobre extendendo o BasePermission
# Esse return vai depender do grupo do Usuário, 
# se existir vai retornar True, dando permissão


# class DeadlineCustomPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return request.user.is_authenticated
#         return request.user.groups.filter(Q(name='Coordenadores') | Q(name='Admins')).exists()
    
class DeadlineCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('app.view_deadline')
        if request.method == 'POST':
            return request.user.has_perm('app.add_deadline')
        if request.method == 'PUT':
            return request.user.has_perm('app.change_deadline')
        if request.method == 'DELETE':
            return request.user.has_perm('app.delete_deadline')
        return False
        # NESSA APLICAÇÂO os usuários que podem fazer os metodos alem de GET, podem fazer todos
        # Esse retorno também seria válido 👇
        # return request.user.has_perms(['app.add_deadline', 'app.delete_deadline', 'app.change_deadline'])


# Create your views here.
class DealineView(ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = DeadlineSerializer
    permission_classes = (DeadlineCustomPermission,)