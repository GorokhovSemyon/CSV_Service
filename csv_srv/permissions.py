from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверяем, является ли пользователь обычным пользователем (не администратором)
        return request.user.is_staff
