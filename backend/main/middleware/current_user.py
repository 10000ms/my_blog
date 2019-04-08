# -*- coding: utf-8 -*-
from threading import local


_user = local()


class CurrentUserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _user.value = request.user
        return self.get_response(request)


def get_current_user():
    # 判断是否存在属性，避免获取时出错
    if hasattr(_user, 'value'):
        return _user.value
    else:
        return None
