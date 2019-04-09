# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ...serializers.tab import TabSerializer
from ...models.tab import Tab


class TabViewSet(viewsets.ModelViewSet):

    # tabs 不需要分页
    pagination_class = None
    queryset = Tab.objects.all()
    serializer_class = TabSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
