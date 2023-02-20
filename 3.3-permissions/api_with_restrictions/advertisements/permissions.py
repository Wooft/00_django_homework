from rest_framework.permissions import BasePermission


class IsOwnerOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
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

class IsDraft(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            if obj.status == 'DRAFT':
                return request.user == obj.creator