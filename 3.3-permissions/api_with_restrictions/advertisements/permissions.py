from rest_framework.authtoken.admin import User
from rest_framework.permissions import BasePermission


class IsOwnerOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            print(request)
            return True
        if request.method == 'DELETE':
            #Проверка на то, что пользователь явялется администратором
            if request.user.is_staff:
                return True
            else:
                return request.user == obj.creator
        if request.method == 'PATCH':
            if request.user.is_staff:
                return True
            else:
                return request.user == obj.creator
        return request.user == obj.creator
