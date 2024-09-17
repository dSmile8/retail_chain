from rest_framework.permissions import BasePermission


class IsActiveUser(BasePermission):
    # Разрешить доступ только активным сотрудникам
    def has_permission(self, request, view):
        return request.user and request.user.is_active
