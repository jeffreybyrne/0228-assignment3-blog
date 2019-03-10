from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime, date


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateField()
    author = models.CharField(max_length=255)

    def clean(self):
        if len(self.body) < 2:
            raise ValidationError('The body must be more than one character.')
        elif self.draft and self.published_date > date.today():
            raise ValidationError('If this is a draft, the publish date must be in the future.')

    def __str__(self):
        return "\"{}\" by {}".format(self.title, self.author)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['author', 'title', 'body', 'draft', 'published_date']


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
