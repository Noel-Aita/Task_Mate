# tasks/permissions.py
from rest_framework import permissions

class IsTaskOwnerOrAssigned(permissions.BasePermission):
    """
    Custom permission:
    - Task creator can edit/delete
    - Assigned technician can view/update status
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return obj.assigned_to == request.user or obj.created_by == request.user
        # For editing/deleting
        return obj.created_by == request.user
