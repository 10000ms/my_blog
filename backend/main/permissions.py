# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    作者可编辑，不然只读
    """

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.pk and
            request.user.is_author
        )


class ReadOnly(permissions.BasePermission):
    """
    只读权限
    """

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)
