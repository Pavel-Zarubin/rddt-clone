from django.urls import path
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView,
                    CreatePostComment,)
from django_filters.views import FilterView
from .filters import PostFilter

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list_All'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', CreatePostComment.as_view(), name='add_comment'),
    path('submit/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('table', FilterView.as_view(filterset_class=PostFilter), name='post_filter'),

]