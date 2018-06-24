from django.shortcuts import render
from django_blog.core.models import Post


def home(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'index.html', {'posts':posts})
