from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppViewSet, SdkViewSet, AppSdkViewSet, CurrentSDKAppStatisticsViewSet, SDKAppListViewSet

router = DefaultRouter()
router.register('apps', AppViewSet, basename="apps")
router.register('sdks', SdkViewSet, basename='sdks')
router.register('app_sdks', AppSdkViewSet, basename='appsdks')
router.register('current_sdk_apps_stat', CurrentSDKAppStatisticsViewSet, basename='current_sdk_apps_stat')
router.register('sdk_apps_list', SDKAppListViewSet, basename='sdk_app_list')
urlpatterns = [
    path('api/', include(router.urls))
]