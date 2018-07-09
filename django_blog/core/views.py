from django.shortcuts import render, get_object_or_404, redirect

from django_blog.core.forms import PostNew
from django_blog.core.models import Post


def home(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'index.html', {'posts': posts})


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'detail_post.html', {'post': posts})


def post_new(request):
    if request.method == "POST":
        form = PostNew(request.POST)
        if form.is_valid():
            form.full_clean()
            new_post = Post.objects.create(author=request.user)
            post = PostNew(request.POST, instance=new_post)
            post.save()
            return redirect('/')
    else:
        form = PostNew()
    return render(request, 'post_new.html', {'form': form})
