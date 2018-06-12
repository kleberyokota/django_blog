from django_blog.core.models import Post


def test_model_field_name():
    f = [f.name for f in Post._meta.get_fields()]
    assert sorted(f) == sorted(['id','title', 'text', 'author', 'created_date', 'published_date'])

