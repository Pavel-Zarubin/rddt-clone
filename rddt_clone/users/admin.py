from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'gender', 'email', 'inn']
    ordering = ['username']
    actions = ['fem_invasion']

    def fem_invasion(self, request, queryset):
        queryset.update(gender='female')
    fem_invasion.short_description = 'Make user a female'

