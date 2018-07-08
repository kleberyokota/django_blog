from django.shortcuts import render, get_object_or_404
from django_blog.core.models import Post


def home(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'index.html', {'posts':posts})

def post_detail(request,pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request,'detail_post.html', {'post': posts})
