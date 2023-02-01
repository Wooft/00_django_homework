from rest_framework.permissions import BasePermission

from advertisements.models import IsAdmin


class IsOwnerOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.method == 'DELETE':
            #Проверка на то, что пользователь явялется администратором
            if IsAdmin.objects.get(user=request.user).isadmin == True:
                return True
            else:
                return request.user == obj.creator
        if request.method == 'PATCH':
            if IsAdmin.objects.get(user=request.user).isadmin == True:
                return True
            else:
                return request.user == obj.creator
        return request.user == obj.creator
