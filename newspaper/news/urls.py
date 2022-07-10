from django.urls import path
from .views import AddPost, EditPost, PostsList, PostDetail, SearchPost, DeletePost

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', SearchPost.as_view()),
    path('add/', AddPost.as_view()),
    path('<int:pk>/edit/', EditPost.as_view()),
    path('<int:pk>/delete/', DeletePost.as_view(), name='post_delete')
]