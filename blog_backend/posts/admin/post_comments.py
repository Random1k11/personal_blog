from django.contrib import admin

from posts.models import PostComments


@admin.register(PostComments)
class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post_id')
