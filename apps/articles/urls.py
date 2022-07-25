from django.conf.urls import include, url

from .views import ArticleRecommendationsView, close_article

urlpatterns = [
    url(r'', ArticleRecommendationsView.as_view(), name='articles'),
    url(r'^close-article/', close_article, name='articles'),
]
