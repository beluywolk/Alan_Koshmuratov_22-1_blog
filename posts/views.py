from django.shortcuts import render
from posts.models import Post, Hashtag

# Create your views here.
def main_page(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)


def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, 'posts/posts.html', context=data)

def hashtags_view(request):
    if request.method == "GET":
        hashtags = Hashtag.objects.all()
        data = {
            'hashtags': hashtags
        }
        return render(request, 'hashtags/hashags.html', context=data)

