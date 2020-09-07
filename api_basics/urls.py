from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # article_list,
    # article_detail,
    ArticleAPIView,
    ArticleDetailAPIView,
    ArticleGenericAPIView,
    ArticleViewSet,
    ArticleGenericViewSet,
    ArticleModelViewSet
)

router = DefaultRouter()
router.register('router', ArticleViewSet, basename='article')
router.register('genericviewset', ArticleGenericViewSet, basename='generic')
router.register('modelviewset', ArticleModelViewSet, basename='model')

urlpatterns = [
    path('', include(router.urls)),
    # path('', article_list),
    path('', ArticleAPIView.as_view()),
    path('generic/<int:pk>/', ArticleGenericAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:pk>/', ArticleDetailAPIView.as_view()),
]
