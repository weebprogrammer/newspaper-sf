from django.views.generic import ListView
from .models import Author, Category, Post, Comment


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


