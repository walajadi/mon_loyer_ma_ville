"""
Permission class to impelement Authentication.
"""
from rest_framework import permissions


class PermissionAccess(permissions.BasePermission):
    """
    Class Permission
    """

    message = "Custom denied message here."

    def has_permission(self, request, view):
        """
        Work on request and/or view here to custom permission
        """
        # False w'd trigger 403 response
        return True
