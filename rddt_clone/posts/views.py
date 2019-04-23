from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment


class PostListAllView(ListView):
    """
    Список всех постов пользователей
    """
    model = Post
    template_name = 'posts/post_list_all.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostListSportView(ListView):
    """
    Список постов пользователей в категории "спорт"
    """
    model = Post
    template_name = 'posts/post_list_sport.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(section='sport')


class PostListCarsView(ListView):
    """
    Список постов пользователей в категории "машины"
    """
    model = Post
    template_name = 'posts/post_list_cars.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(section='cars')


class UserPostListView(ListView):
    """
    Список всех постов конкретного пользователя
    """
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    """
    Страница поста
    """
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Страница создания поста
    """
    model = Post
    fields = ['title', 'content', 'section', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Страница обновления поста
    """
    model = Post
    fields = ['title', 'content', 'section', 'image']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Страница удаления поста
    """
    model = Post

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CreatePostComment(CreateView):
    """
    Страница создания комментария
    """
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('posts:list')




















