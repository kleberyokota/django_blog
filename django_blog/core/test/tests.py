import pytest

from django_blog.core.models import Post
from django_blog.django_assertions import dj_assert_template_used, dj_assert_contains, dj_assert_subtest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_get(client):
    request = client.get('/')
    assert request.status_code == 200

@pytest.mark.django_db
def test_templated(client):
    request = client.get('/')
    dj_assert_template_used(request,'index.html')

@pytest.mark.django_db
def test_context(client):
    request = client.get('/')
    dj_assert_contains(request,'<h1>')

@pytest.mark.django_db
def test_post_tittle_in_html(client):
    User.objects.create_user('kleber', 'kleber_yokota@hotmail.com', 'aaa')
    title = 'teste titulo'
    text = 'teste texto'
    author = User.objects.get(pk=1)
    Post.objects.create_post(title=title, text=text, author=author)
    request = client.get('/')
    dj_assert_contains(request,'teste titulo', 1)

@pytest.mark.django_db
def test_post_text_in_html(client):
    User.objects.create_user('kleber', 'kleber_yokota@hotmail.com', 'aaa')
    title = 'teste titulo'
    text = 'teste texto'
    author = User.objects.get(pk=1)
    Post.objects.create_post(title=title, text=text, author=author)
    request = client.get('/')
    dj_assert_contains(request,'teste text', 1)
