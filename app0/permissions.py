# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class HighFlexibilityPermission(BasePermission):
    def has_permission(self, request, view):
        """
        根據需求, request和view制定permission規則判斷條件
        """
        # print(type(request.user))
        # print(request.user, request.auth, view)

        if request.user.username == 'admin':
            return True

        return False


class GroupPermission(BasePermission):
    def has_permission(self, request, view):
        for group in request.user.groups.all():
            if group.name.lower() == 'vip':
                return True
        return False
