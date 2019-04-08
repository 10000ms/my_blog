# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.rest.user.UserViewSet)
router.register(r'blog', views.rest.blog.BlogViewSet)
router.register(r'category', views.rest.category.CategoryViewSet)
router.register(r'comment', views.rest.comment.CommentViewSet)
router.register(r'tab', views.rest.tab.TabViewSet)
router.register(r'website-manage', views.rest.website_manage.WebsiteManageViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'index/', views.main_index.MainIndex.as_view()),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
