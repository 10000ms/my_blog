from django.shortcuts import render

# Create your views here.


def bad_request(request):
    return render(request, 'error.html', status=400)
