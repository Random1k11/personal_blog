from django.db import models


class PostCategories(models.Model):
    label = models.CharField(max_length=2048)
    description = models.TextField()
