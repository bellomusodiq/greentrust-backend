from rest_framework.permissions import BasePermission

class StaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method is "GET":
            return True
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method is "GET":
            return True
        return request.user.is_staff

class StaffAndCreatedUser(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method is "GET":
            return True
        return request.user.is_staff or (request.user == obj.paid_by) or (request.user == obj.user) 