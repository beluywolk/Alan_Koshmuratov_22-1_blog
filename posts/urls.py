from django.urls import path
from posts.views import posts_view,  detail_view, hashtag_view, posts_create_view



urlpatterns = [
    path('posts/', posts_view),
    path('hashtags/', hashtag_view),
    path('posts/<int:id>', detail_view),
    path('posts/create', posts_create_view)
]