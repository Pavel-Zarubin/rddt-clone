from django_filters import FilterSet
from .models import User


class UsersFilter(FilterSet):
    """
    Фильтр пользователей по полу
    """
    class Meta:
        model = User
        fields = ('gender', )

