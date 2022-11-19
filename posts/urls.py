from django.urls import path
from posts.views import posts_view, hashtags_view, detail_view



urlpatterns = [
    path('posts/', posts_view),
    path('hashtags/', hashtags_view),
    path('posts/<int:id>', detail_view)
]