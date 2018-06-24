import pytest

from django.contrib.auth.models import User
from django_blog.core.models import Post


def test_model_field_name():
    f = [f.name for f in Post._meta.get_fields()]
    assert sorted(f) == sorted(['id','title', 'text', 'author', 'created_date', 'published_date'])

@pytest.mark.django_db
def test_create_post():
    User.objects.create_user('kleber', 'kleber_yokota@hotmail.com', 'aaa')
    title = 'a'*100
    text = 'abcs kamslkm dokd;s odf, lmmsd'
    author = User.objects.get(pk=1)
    Post.objects.create_post(title=title, text=text,author=author)
    assert len(Post.objects.all()) == 1
