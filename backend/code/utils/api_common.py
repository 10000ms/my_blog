# -*- coding: utf-8 -*-


def create_response(code=200, msg=None, data=None, **kwargs):
    """
    創建通用的返回dict
    """
    r = {
        'code': code,
        'msg': msg,
        'data': data,
    }
    r.update(kwargs)
    return r
