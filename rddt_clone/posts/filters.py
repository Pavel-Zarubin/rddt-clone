from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    """
    Фильтр тиаблицы постов по автору поста
    """
    class Meta:
        model = Post
        fields = ['author',]

