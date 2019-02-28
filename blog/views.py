from django.http import HttpResponse
from django.shortcuts import render
import datetime


def home_page(request):
    now = str(datetime.datetime.now())
    context = {'name': 'Jeff', 'day': now}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
