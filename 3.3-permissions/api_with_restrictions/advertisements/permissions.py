from rest_framework.permissions import BasePermission


class IsOwnerOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.method == 'DELETE':
            return request.user == obj.creator
        if request.method == 'PATCH':
            return request.user == obj.creator
        return request.user == obj.owner