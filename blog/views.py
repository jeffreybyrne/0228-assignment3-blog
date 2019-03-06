from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Article
import datetime


def home_page(request):
    now = str(datetime.datetime.now())
    articles = Article.objects.filter(draft=False).order_by('-published_date').all()
    context = {'name': 'Jeff', 'day': now, 'articles': articles}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def home_page_redirect(request):
    return redirect(home_page)


def blog_post(request, id):
    post = get_object_or_404(Article, pk=id)
    context = {'article': post}
    html = render(request, 'post.html', context)
    return HttpResponse(html)


def new_comment(request):
    pass
