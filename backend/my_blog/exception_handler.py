# -*- coding: utf-8 -*-
from rest_framework.views import exception_handler

from utils.api_common import create_response


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:

        errors = []
        message = response.data.get('detail')
        if not message:
            for field, value in response.data.items():
                errors.append('{} : {}'.format(field, ' '.join(value)))
            response.data = create_response(code=response.status_code, msg=errors)
        else:
            response.data = create_response(code=response.status_code, msg=message)

    return response
