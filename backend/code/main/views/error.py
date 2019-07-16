from django.shortcuts import render
from django.views.decorators.cache import cache_page


# 404页面不会改，直接缓存一天就行了
@cache_page(60 * 60 * 24)
def bad_request(request, exception):
    # for i in request.META:
    #     print('{} = {}'.format(i, request.META[i]))
    return render(request, 'error.html', status=404)
