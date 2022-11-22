from django.urls import path
from posts.views import posts_view,  detail_view, hashtag_view



urlpatterns = [
    path('posts/', posts_view),
    path('hashtags/', hashtag_view),
    path('posts/<int:id>', detail_view)
]