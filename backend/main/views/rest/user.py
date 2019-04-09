# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ...serializers.user import UserSerializer
from ...permissions import OpenRegister
from ...models.user import User


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser | OpenRegister, )
