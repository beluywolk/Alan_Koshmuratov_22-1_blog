from django.shortcuts import render, redirect
from posts.models import Post, Hashtag, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from users.utills import get_user_from_request

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
        hashtag_id = request.GET.get('hashtag_id')
        if hashtag_id:
            posts = Post.objects.filter(hashtag_id=hashtag_id)
        else:
            posts = Post.objects.all()
        data = {
            'posts': posts,
            'user': get_user_from_request(request)
        }
        return render(request, 'posts/posts.html', context=data)




def detail_view(request, **kwargs):
    if request.method == "GET":
        post = Post.objects.get(id=kwargs['id'])
        comment = Comment.objects.filter(post=post)

        data = {
            'post': post,
            'comment': comment,
            'form': CommentCreateForm

        }
        return render(request, 'posts/detail.html', context=data)
    if request.method == 'POST':
        form = CommentCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=1,
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f'/posts/{kwargs["id"]}/')
        else:
            post = Post.objects.get(id=kwargs['id'])
            comment = Comment.objects.filter(post=post)

            data = {
                'post': post,
                'comment': comment,
                'form': form
            }
            return render(request, 'products/detail.html', context=data)


def hashtag_view(request, **kwargs):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        data = {
            'hashtags': hashtags
        }

        return render(request, 'hashtags/hashags.html', context=data)


def posts_create_view(request):
    if request.method == 'GET':
        data = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context=data)
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),
                likes=form.cleaned_data.get('likes'),
                hashtag_id=form.cleaned_data.get('hashtag')
            )
            return redirect('/posts')
        else:
            data = {
                'form': form
            }
            return render(request, 'posts/create.html', context=data)

