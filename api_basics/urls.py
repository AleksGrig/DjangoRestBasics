from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailAPIView

urlpatterns = [
    # path('', article_list),
    path('', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:pk>/', ArticleDetailAPIView.as_view()),
]
