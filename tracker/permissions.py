from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        queryset = view.get_queryset()
        user = request.user
        return queryset.filter(user=user).exists()