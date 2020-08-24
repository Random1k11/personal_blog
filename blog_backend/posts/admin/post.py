from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ('updated_at', )
    list_display = ('title', 'active', 'updated_at', 'created_at')
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
