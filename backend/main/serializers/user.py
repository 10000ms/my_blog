# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.user import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'profile',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'is_author',
            'is_superuser',
        )
        # 用户资料修改不是全部统一修改
        extra_kwargs = {
            'profile': {'required': False},
            'username': {'required': False},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'is_author': {'required': False},
            'is_superuser': {'required': False},
        }
