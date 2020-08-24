from datetime import datetime

from django.db import models

from .post_categories import PostCategories


class Post(models.Model):
    title = models.CharField(max_length=2048)
    text = models.TextField()
    image = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(PostCategories, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
