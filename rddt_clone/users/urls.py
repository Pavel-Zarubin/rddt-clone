from django.urls import path
from . import views
from .views import ProfileListView

app_name = 'users'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
]