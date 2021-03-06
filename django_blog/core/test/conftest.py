import pytest
from django.contrib.auth.models import User

from django_blog.core.models import Post


@pytest.fixture()
def usuario(db):
    user = User.objects.create_user(username='kleber', email='kleber_yokota@hotmail.com', password='aaa')
    user.save()
    return user


@pytest.fixture()
def db_post(db, usuario):
    title = 'teste titulo 1'
    text = 'teste texto 1'
    author = User.objects.get(pk=1)
    post = Post(title=title, text=text, author=author)
    post.save()

    title = 'teste titulo 2'
    text = 'teste texto 2'
    author = User.objects.get(pk=1)
    post = Post(title=title, text=text, author=author)
    post.save()

    return post
