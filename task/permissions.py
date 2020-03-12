from rest_framework.permissions import BasePermission
from task.models import Task


class Isowner(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return Task.objects.filter(pk=view.kwargs.get('pk'), owner=request.user).exists()
