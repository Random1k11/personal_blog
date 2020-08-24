from django.db import models

from .post import Post


class PostComments(models.Model):
    comment = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
