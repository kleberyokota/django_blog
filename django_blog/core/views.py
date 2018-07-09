from django.shortcuts import render, get_object_or_404, redirect
from django_blog.core.models import Post
from django.utils import timezone
from django_blog.core.forms import PostNew
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'index.html', {'posts':posts})


def post_detail(request,pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request,'detail_post.html', {'post': posts})


def post_new(request):
    if request.method =="POST":
        form = PostNew(request.POST)
        if form.is_valid():
            post = PostNew(request.POST)
            post.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostNew()
    return render(request, 'post_new.html',{'form':form})
