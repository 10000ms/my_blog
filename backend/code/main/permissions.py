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


class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    只允许创建者编辑
    """

    def has_object_permission(self, request, view, obj):
        # 允许所有非修改的安全方法
        if request.method in permissions.SAFE_METHODS:
            return True
        # 剩下的修改非安全方法只允许创建者进行修改
        return obj.creator == request.user


class NoDemoUser(permissions.BasePermission):
    """
    demo用户不允许使用非安全方法
    """

    def has_permission(self, request, view):
        # 允许所有非修改的安全方法
        if request.method in permissions.SAFE_METHODS:
            return True
        return not request.user.is_demo_user


class UserCannotDelete(permissions.BasePermission):
    """
    普通用户没有删除权限
    """

    def has_permission(self, request, view):
        return not (request.method == 'DELETE' and not request.user.is_staff)
