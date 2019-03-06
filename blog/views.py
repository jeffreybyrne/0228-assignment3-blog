from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Article, Comment
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
    if post.comments.count() > 0:
        comment_count = True
    else:
        comment_count = False
    context = {'article': post, 'comments': comment_count}
    html = render(request, 'post.html', context)
    return HttpResponse(html)


def create_comment(request):
    comment_name = request.POST['comment_name']
    comment_message = request.POST['comment_message']
    comment_article = Article.objects.get(pk=request.POST['post_num'])
    new_comment = Comment.objects.create(name=comment_name,
                                         message=comment_message,
                                         article=comment_article)
    return HttpResponseRedirect('/post/' + request.POST['post_num'])
