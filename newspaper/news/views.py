from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, Comment


class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-id']


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


