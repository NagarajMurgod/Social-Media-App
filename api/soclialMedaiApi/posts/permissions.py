from rest_framework import permissions


class IsPostOwner(permissions.BasePermission):
    def has_object_permission(self, request, views, obj):
        return obj.user == request.user 