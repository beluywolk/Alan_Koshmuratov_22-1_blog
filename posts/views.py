from django.shortcuts import render, redirect
from posts.models import Post, Hashtag, Comment
from posts.forms import PostCreateForm, CommentCreateForm
from users.utills import get_user_from_request
from django.views.generic import ListView, CreateView


PAGINATION_LIMIT = 4




class MainPage(ListView):
    template_name = 'layouts/main.html'
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, self.template_name, context=data)





class PostView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'posts/posts.html'
    def get(self, request, *args, **kwargs):
        hashtag_id = request.GET.get('hashtag_id')
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if hashtag_id and hashtag_id != 'None':
            posts = self.model.objects.filter(hashtag_id=hashtag_id)
        else:
            posts = self.model.objects.all()
        if search_text:
            posts = posts.filter(title__icontains=search_text)

        max_page = round(posts.__len__ / PAGINATION_LIMIT)

        posts = posts[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        data = {
            'posts': posts,
            'user': get_user_from_request(request),
            'hashtag_id': hashtag_id,
            'current page': page,
            'max_page': range(1, max_page + 1)
        }
        return render(request, self.template_name, context=data)






class DetailView(ListView):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['id'])
        comment = Comment.objects.filter(post=post)

        data = {
            'post': post,
            'comment': comment,
            'form': CommentCreateForm

        }
        return render(request, 'posts/detail.html', context=data)
    def post(self, request, *args, **kwargs):


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





class HashtagsView(ListView):
    model = Hashtag
    queryset = Hashtag.objects.all()
    template_name = 'hashtags/hashags.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'object_list': self.get_queryset(),
            'user': get_user_from_request(self.request)
        }

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_queryset(),
            'user': get_user_from_request(request)
        }
        return render(request, self.template_name, context=context)



class PostCreateView(ListView, CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'user': get_user_from_request(self.request)
        }
    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):


        form = self.form_class(data=request.POST)
        if form.is_valid():
            self.model.objects.create(
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),
                likes=form.cleaned_data.get('likes'),
                hashtag_id=form.cleaned_data.get('hashtag')
            )
            return redirect('/posts')

            return render(request, self.template_name, context=self.get_context_data(form=form))




