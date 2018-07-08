import pytest
from django_blog.django_assertions import dj_assert_template_used, dj_assert_contains, dj_assert_not_contains


@pytest.fixture
def resp(client,db_post):
    return client.get('/post/1/')

def test_post_detail(resp):
    assert resp.status_code == 200


def test_templated(resp):
    dj_assert_template_used(resp,'detail_post.html')


def test_post_tittle_in_html(resp):
    dj_assert_contains(resp,'teste titulo 1', 1)


def test_post_tittle_not_in_html(resp):
    dj_assert_not_contains(resp,'teste titulo 2')
