from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'date_posted']
    ordering = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'date_posted']
    ordering = ['post']
    actions = ['my_custom_action']

    def my_custom_action(self, request, queryset):
        return True
    my_custom_action.short_description = 'Custom'
