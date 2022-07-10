from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import PostForm
from .models import Author, Category, Post, Comment
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 1

   


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class SearchPost(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context 


class AddPost(ListView):
    model = Post
    template_name = 'add.html'
    context_object_name = 'news'
    form_class = PostForm

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
 
        context['form'] = PostForm()
        return context
 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) # создаём новую форму, забиваем в неё данные из POST-запроса 
 
        if form.is_valid(): # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем новый товар
            form.save()
 
        return super().get(request, *args, **kwargs)

class EditPost(UpdateView):
    model = Post
    template_name = 'edit.html'
    form_class = PostForm
    context_object_name = 'news'
    success_url = '/news/'


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class DeletePost(DeleteView):
    queryset = Post.objects.all()
    template_name = 'delete.html'
    success_url = '/news/'