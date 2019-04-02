# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.rest_test.UserViewSet)
router.register(r'groups', views.rest_test.GroupViewSet)
router.register(r'blog', views.rest_test.BlogViewSet)
router.register(r'category', views.rest_test.CategoryViewSet)
router.register(r'tab', views.rest_test.TabViewSet)
router.register(r'website-manage', views.rest_test.WebsiteManageViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('index/', views.main_index.MainIndex.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
