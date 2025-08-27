from rest_framework import permissions

class IsTaskOwnerOrAssigned(permissions.BasePermission):
    """
    - Task creator can edit/delete
    - Assigned technician can view/update status
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.assigned_to == request.user or obj.created_by == request.user
        return obj.created_by == request.user
