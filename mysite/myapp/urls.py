from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import article_list, article_details
# from .views import ArticleList, ArticleDetail
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AppViewSet, SdkViewSet, AppSdkViewSet,CurrentSDKAppStatisticsViewSet
# from .views import ArticleDetailViewSet

router = DefaultRouter()
router.register('apps', AppViewSet, basename="apps")
router.register('sdks', SdkViewSet, basename='sdks')
router.register('app_sdks', AppSdkViewSet, basename='appsdks')
router.register('current_sdk_apps_stat', CurrentSDKAppStatisticsViewSet, basename='current_sdk_apps_stat')

urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:pk>/', ArticleDetail.as_view())
    path('api/', include(router.urls))
]