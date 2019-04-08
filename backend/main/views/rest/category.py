# -*- coding: utf-8 -*-
from rest_framework import (
    viewsets,
    permissions,
)

from ... import serializers
from ...models.category import Category


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = serializers.category.CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
