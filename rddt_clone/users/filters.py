import django_filters
from .models import User


class UsersFilter(django_filters.FilterSet):

    class Meta:

        model = User
        fields = ('gender', )

