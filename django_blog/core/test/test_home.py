import pytest

from django_blog.django_assertions import dj_assert_template_used, dj_assert_contains


@pytest.fixture
def resp(client, db_post):
    return client.get('/')


def test_get(resp):
    assert resp.status_code == 200


def test_templated(resp):
    dj_assert_template_used(resp, 'index.html')


def test_context(resp):
    dj_assert_contains(resp, '<h1>')


def test_post_tittle_in_html(resp):
    dj_assert_contains(resp, 'teste titulo', 2)


def test_post_text_in_html(resp):
    dj_assert_contains(resp, 'teste text', 2)


def test_create_post_1(resp):
    dj_assert_contains(resp, '<a href="/post/1/"', 1)


def test_create_post_2(resp):
    dj_assert_contains(resp, '<a href="/post/2/"', 1)
