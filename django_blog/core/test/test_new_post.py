import pytest
from django.contrib.auth.models import User

from django_blog.core.models import Post
from django_blog.django_assertions import dj_assert_contains


@pytest.fixture()
def resp(client, db_post):
    return client.get('/post/new/')


def test_new_post(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'content,qtd', [
        ('<label', 2),
        ('Text:</label>', 1),
        ('Title:</label>', 1),
        ('<form', 1),
        ('method="POST"', 1),
        ('<textarea', 1),
        ('<input', 2)]
)
def test_has_field(client, db_post, content, qtd):
    client.login(username='kleber', password='aaa')
    dj_assert_contains(client.get('/post/new/'), content, qtd)


def test_valid_new_post(client, db_post, db):
    client.login(username='kleber', password='aaa')
    data = {
        "title": "titulo criado 1",
        "text": "texto criacao 1"
    }
    client.post('/post/new/', data)
    assert len(Post.objects.all()) == 3


def test_invalid_new_post(client, db_post):
    user = User.objects.create_user(username='kleber1', email='kleber_yokota@hotmail.com', password='aaa')
    user.save()
    client.login(username='kleber1', password='aaa')
    title = 't' * 201
    data = {
        "title": title,
        "text": "texto criacao 1"
    }
    client.post('/post/new/', data)
    assert len(Post.objects.all()) == 2


def test_redirect(client, db_post, db):
    client.login(username='kleber', password='aaa')
    data = {
        "title": "titulo criado 1",
        "text": "texto criacao 1"
    }
    resp = client.post('/post/new/', data)
    assert resp.status_code == 302
