# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from ...serializers.tab import TabSerializer
from ...models.tab import Tab


class TabViewSet(ModelViewSet):

    # tabs 不需要分页
    pagination_class = None
    queryset = Tab.objects.all()
    serializer_class = TabSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
