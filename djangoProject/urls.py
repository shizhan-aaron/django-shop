"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, re_path, include
import xadmin
from djangoProject.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodListViewSet, CategoryViewSet, BannerViewSet, IndexCategoryViewSet
from user.views import UserViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet

router = DefaultRouter()
router.register(r'goods', GoodListViewSet, basename='goods')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'users', UserViewSet, basename='users')
router.register(r'userfavs', UserFavViewSet, basename='userfavs')
router.register(r'messages', LeavingMessageViewSet, basename='messages')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'banners', BannerViewSet, basename='banners')
router.register(r'indexgoods', IndexCategoryViewSet, basename='indexgoods')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    path('', include(router.urls)),

    # drf
    path('docs/', include_docs_urls(title='aaaaaa')),
    path('api-auth/', include('rest_framework.urls')),

    # DRF自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),

    # jwt认证模式
    path('login/', obtain_jwt_token),
]
