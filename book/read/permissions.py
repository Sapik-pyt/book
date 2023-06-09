from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Удалить и редактировать может тоьлько автор книги.
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
