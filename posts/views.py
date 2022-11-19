from django.shortcuts import render, HttpResponse
from posts.models import Post, Hashtag, Comment

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


def detail_view(request, **kwargs):
    if request.method == "GET":
        post = Post.objects.get(id=kwargs['id'])
        comment = Comment.objects.filter(post=post)

        data = {
            'post': post,
             'comment': comment
        }
        return render(request, 'posts/detail.html', context=data)


