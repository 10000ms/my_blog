# -*- coding: utf-8 -*-
from rest_framework import permissions

from .models.website_manage import WebsiteManage


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    作者可编辑，不然只读
    """

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_author
        )


class ReadOnly(permissions.BasePermission):
    """
    只读权限
    """

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)


class OpenRegister(permissions.BasePermission):
    """
    是否开发注册的权限
    """

    def has_permission(self, request, view):
        res = False
        p = WebsiteManage.objects.all()[:1]
        if p and p.open_register:
            res = True
        return bool(request.method == 'POST' and res)
