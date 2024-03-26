from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Author').exists()

    # def has_object_permission(self, request, view, obj):
    #     return request.user.groups.filter(name='Author').exists()