# import ipdb
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Article, CommentForm, ArticleForm
from blog.forms import LoginForm
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
    new_form = CommentForm(initial={'article': id})
    context = {'article': post, 'comments': comment_count, 'form': new_form}
    html = render(request, 'post.html', context)
    return HttpResponse(html)


# def new_article_page(request):
#     new_form = ArticleForm()
#     context = {'form': new_form}
#     html = render(request, 'create.html', context)
#     return HttpResponse(html)
#

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.user = request.user
            new_article = form.save()
            return HttpResponseRedirect('/post/' + str(new_article.id))
    else:
        form = ArticleForm()
    response = render(request, 'create.html', {'form': form})
    return HttpResponse(response)


@login_required
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            new_article.user = request.user
            new_article.save()
            return HttpResponseRedirect('/post/{}'.format(new_article.id))
    else:
        form = ArticleForm()
    response = render(request, 'create.html', {'form': form})
    return HttpResponse(response)


def create_comment(request):
    # comment_name = request.POST['comment_name']
    # comment_message = request.POST['comment_message']
    # comment_article = Article.objects.get(pk=request.POST['post_num'])
    # new_comment = Comment.objects.create(name=comment_name,
    #                                      message=comment_message,
    #                                      article=comment_article)
    # return HttpResponseRedirect('/post/' + request.POST['post_num'])
    form = CommentForm(request.POST)
    # ipdb.set_trace()
    # form['article'] = request.POST['article']
    if form.is_valid():
        new_comment = form.save()
        return HttpResponseRedirect('/post/' + request.POST['article'])
    else:
        print(form.errors)
        response = render(request, 'index.html')
        return HttpResponse(response)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()
    context = {'form': form}
    response = render(request, 'login.html', context)
    return HttpResponse(response)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home')


def edit_blog_post(request, id):
    pass
