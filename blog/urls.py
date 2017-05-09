from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views

urlpatterns = [
    url(r'^$',
        ListView.as_view(queryset=Post.objects.all().order_by("-date")[:10],
            template_name="blog/blog.html"
        )
    ),
    url(r'^post/$', views.post, name="post")
]
