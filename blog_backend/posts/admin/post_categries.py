from django.contrib import admin

from posts.models import PostCategories


@admin.register(PostCategories)
class PostCategoriesAdmin(admin.ModelAdmin):
    list_display = ('label', 'description')
