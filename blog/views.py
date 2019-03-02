from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article
import datetime


def home_page(request):
    now = str(datetime.datetime.now())
    articles = Article.objects.filter(draft=False).order_by('-published_date').all()
    context = {'name': 'Jeff', 'day': now, 'articles': articles}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
