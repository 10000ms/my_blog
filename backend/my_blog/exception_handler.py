# -*- coding: utf-8 -*-
from rest_framework.views import exception_handler

from utils.api_common import create_response


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None:
        response.data = create_response(code=response.status_code, msg=exc.detail)
    return response
