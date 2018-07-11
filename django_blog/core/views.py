from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django_blog.core.forms import PostForm
from django_blog.core.models import Post


def home(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'detail_post.html', {'post': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.full_clean()
            new_post = Post.objects.create(author=request.user)
            post = PostForm(request.POST, instance=new_post)
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.full_clean()
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/post/' + str(pk) + '/')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_new.html', {'form': form})
