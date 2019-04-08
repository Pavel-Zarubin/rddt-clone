from django.contrib import admin
from .models import User

admin.site.register(User)

def fem_invasion(self, request, queryset):
        queryset.update(first_name='female')


admin.site.add_action(fem_invasion, 'Make user a female')