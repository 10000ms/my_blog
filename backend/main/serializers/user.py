# -*- coding: utf-8 -*-
from rest_framework import serializers

from ..models.user import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'groups',
            'is_author',
            'is_superuser',
        )
