"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blog.views import home_page, blog_post, home_page_redirect, create_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page, name='home'),
    path('', home_page_redirect),
    path('post/<int:id>', blog_post, name='blog_post'),
    path('post/comment/', create_comment, name='create_comment')
]
