from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'gender', 'email', 'inn']
    ordering = ['username']
    actions = ['fem_attack', 'male_attack']

    def fem_attack(self, request, queryset):
        female = User.objects.filter(gender='female').count()
        male = User.objects.filter(gender='male').count()

        if female < male:
            dif = (male - female)//2
            male = User.objects.filter(gender='male')[:dif]
            User.objects.filter(id__in=male).update(gender='female')
        else:
            return False

    def male_attack(self, request, queryset):
        female = User.objects.filter(gender='female').count()
        male = User.objects.filter(gender='male').count()

        if male < female:
            dif = (female - male)//2
            male = User.objects.filter(gender='female')[:dif]
            User.objects.filter(id__in=male).update(gender='male')
