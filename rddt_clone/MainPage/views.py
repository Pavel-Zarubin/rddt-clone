from django.shortcuts import render
from .models import Post


def posts_list(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'MainPage/mainpage.html', context)

