# -*- coding: utf-8 -*-
from django.shortcuts import render


def bad_request(request, exception):
    # for i in request.META:
    #     print('{} = {}'.format(i, request.META[i]))
    return render(request, 'error.html', status=404)
