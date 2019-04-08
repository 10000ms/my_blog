# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ... import serializers
from ... import permissions as custom_permissions
from ...models.user import User


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.user.UserSerializer
    permission_classes = (permissions.IsAdminUser | custom_permissions.OpenRegister, )
