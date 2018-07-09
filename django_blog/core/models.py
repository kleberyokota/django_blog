from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def create_post(self, title, text, author, created_date):
        post = Post(
            title=title,
            text=text,
            author=author
        )

        if post.full_clean():
            return self.create(
                title=title,
                text=text,
                author=author
            )

        post = self.create(
            title=title,
            text=text,
            author=author
        )

        return post


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    objects = PostManager()

    def __str__(self):
        return self.title
