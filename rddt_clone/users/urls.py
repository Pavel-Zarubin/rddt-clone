from django.urls import path
from . import views
from .views import ProfileListView

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
]