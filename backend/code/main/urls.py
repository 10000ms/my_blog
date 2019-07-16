from django.urls import include, path
from django.conf import settings
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'user', views.rest.user.UserViewSet)
router.register(r'blog', views.rest.blog.BlogViewSet)
router.register(r'category', views.rest.category.CategoryViewSet)
router.register(r'comment', views.rest.comment.CommentViewSet)
router.register(r'tab', views.rest.tab.TabViewSet)
router.register(r'website-manage', views.rest.website_manage.WebsiteManageViewSet)
router.register(r'about-me', views.rest.about_me.AboutMeViewSet, basename='about_me')


urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/init-index/', views.init_index.InitIndex.as_view()),
]

if settings.DEBUG:
    urlpatterns.append(path(r'api/test/', views.test.Test.as_view()))
    urlpatterns.append(path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')))
