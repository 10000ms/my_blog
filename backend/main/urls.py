# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.rest.UserViewSet)
router.register(r'blog', views.rest.BlogViewSet)
router.register(r'category', views.rest.CategoryViewSet)
router.register(r'tab', views.rest.TabViewSet)
router.register(r'website-manage', views.rest.WebsiteManageViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'index/', views.main_index.MainIndex.as_view()),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
