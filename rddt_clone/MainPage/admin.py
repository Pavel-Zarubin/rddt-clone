from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'date_posted']
    actions = ['my_custom_actino']

    def my_custom_action(self, request, queryset):
        return True
    my_custom_action.short_description = 'Custom'
