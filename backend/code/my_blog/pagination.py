# -*- coding: utf-8 -*-
from rest_framework import pagination
from rest_framework.response import Response

from utils.api_common import create_response


class CustomPagination(pagination.PageNumberPagination):
    """
    改变默认的分页返回格式
    """

    def get_paginated_response(self, data):
        page = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
        }
        r = create_response(data=data, page=page)
        return Response(r)
