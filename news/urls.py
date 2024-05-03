from django.urls import path, re_path
from django.conf.urls import include
from django.views.generic import ListView, DetailView
from news.models import Articles

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    re_path('^(?P<pk>\d+)/$', DetailView.as_view(model=Articles, template_name="news/post.html"))
]

