from django.db import models
from django import forms


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return "\"{}\" by {}".format(self.title, self.author)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['author', 'title', 'body', 'draft']


class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        widgets = {'article': forms.HiddenInput()}
        fields = ['name', 'message', 'article']
