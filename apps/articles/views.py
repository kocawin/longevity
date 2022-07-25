from django.views import *
from django.shortcuts import render
from apps.articles.models import Article, LessInterestArticles
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse


class ArticleRecommendationsView(View):
    @method_decorator(login_required(login_url='/admin/'))
    def get(self, request):
        from apps.recommenders.recommender import get_articles_recommendations
        articles = get_articles_recommendations(LessInterestArticles.objects.all())
        return render(request, 'articles/articles.html', dict(articles=articles))


@login_required(login_url='/admin/')
def close_article(request):
    args = request.GET.get('article_id')
    article = Article.objects.get(pk=args)
    print(article)
    if article is not None:
        if not LessInterestArticles.objects.filter(article=article, user=request.user).exists():
            LessInterestArticles(article=article, user=request.user).save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error', 'msg': 'Article not found'})
