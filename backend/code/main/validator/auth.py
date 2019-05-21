# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError


def validate_username_password(value):
    if not 6 <= len(value) <= 20:
        raise ValidationError(
            '用户名或密码长度必须是6-20个字符',
            params={'value': value},
        )


def validate_name(value):
    if not 1 <= len(value) <= 20:
        raise ValidationError(
            '姓或名必须1-20个字符',
            params={'value': value},
        )


def validate_phone(value):
    if not 6 <= len(value) <= 20:
        raise ValidationError(
            '电话格式错误',
            params={'value': value},
        )
