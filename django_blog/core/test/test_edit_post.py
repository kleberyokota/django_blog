import pytest

from django_blog.core.models import Post
from django_blog.django_assertions import dj_assert_contains


def test_resp(client, db_post):
    resp = client.get('/post/1/edit/')
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'content,qtd', [
        ('teste titulo 1', 1),
        ('teste texto 1', 1)
    ]
)
def test_load_edit(client, db_post, content, qtd):
    client.login(username='kleber', password='aaa')
    resp = client.get('/post/1/edit/')
    dj_assert_contains(resp, content, qtd)


def test_title_edit(client, db_post):
    client.login(username='kleber', password='aaa')
    resp = client.get('/post/1/edit/')
    r = resp.context['form']
    data = r.initial
    data['title'] = 'titulo editado 1'
    client.post('/post/1/edit/', data)
    db_obj = Post.objects.get(id=1)
    assert db_obj.title == 'titulo editado 1'


def test_text_edit(client, db_post):
    client.login(username='kleber', password='aaa')
    resp = client.get('/post/1/edit/')
    r = resp.context['form']
    data = r.initial
    data['text'] = 'texto editado 1'
    client.post('/post/1/edit/', data)
    db_obj = Post.objects.get(id=1)
    assert db_obj.text == 'texto editado 1'
