from django.urls import path
from posts.views import PostView,  DetailView, HashtagsView, PostCreateView



urlpatterns = [
    path('posts/', PostView),
    path('hashtags/', HashtagsView.as_view),
    path('posts/<int:id>', DetailView),
    path('posts/create', PostCreateView.as_view)
]