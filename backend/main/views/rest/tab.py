# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ... import serializers
from ...models.tab import Tab


class TabViewSet(viewsets.ModelViewSet):

    # tabs 不需要分页
    pagination_class = None
    queryset = Tab.objects.all()
    serializer_class = serializers.tab.TabSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
