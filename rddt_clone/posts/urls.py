from django.urls import path
from .views import (PostListAllView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView,
                    CreatePostComment, PostListSportView,
                    PostListCarsView)
from django_filters.views import FilterView
from .filters import PostFilter

app_name = 'posts'

urlpatterns = [
    path('', PostListAllView.as_view(), name='list'),
    path('sports/', PostListSportView.as_view(), name='sport'),
    path('cars/', PostListCarsView.as_view(), name='cars'),
    path('by_username/<str:username>', UserPostListView.as_view(), name='list-by-username'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('comment/create/<int:post_pk>', CreatePostComment.as_view(), name='comment-create'),
    path('submit/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('table', FilterView.as_view(filterset_class=PostFilter), name='post-filter'),
]