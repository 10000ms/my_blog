# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework import routers
from main.views import rest_test

router = routers.DefaultRouter()
router.register(r'users', rest_test.UserViewSet)
router.register(r'groups', rest_test.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
