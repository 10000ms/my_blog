from django.core.cache import cache
from django.conf import settings

from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from ...serializers.about_me import AboutMeSerializer
from ...permissions import ReadOnly
from ...models.website_manage import WebsiteManage


class AboutMeViewSet(ModelViewSet):

    # about me 不需要分页
    pagination_class = None
    queryset = WebsiteManage.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = (IsAdminUser | ReadOnly, )

    def list(self, request, *args, **kwargs):
        """
        返回单个对象
        """
        # 缓存
        b = cache.get('about_me')
        if not b:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)

            # 返回单个对象
            res = serializer.data
            if isinstance(res, list) and len(res) > 0:
                res = res[0]

            cache.set('about_me', res, 60 * settings.CACHE_TIME)
            b = res

        return Response(b)
