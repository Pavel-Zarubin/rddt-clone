from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse
from sorl.thumbnail import ImageField


class SectionChoices:
    """
    Разделы
    """
    all = 'all'
    cars = 'cars'
    sport = 'sport'

    CHOICES = (
        (all, "all"),
        (cars, "cars"),
        (sport, "sport")
    )

class Post(models.Model):
    """
    Модель поста
    """
    title = models.CharField('title', max_length=151, db_index=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.CharField(max_length=10, choices=SectionChoices.CHOICES)
    image = ImageField(upload_to="posts/", null=True, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    """
    Модель комментария
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=160)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.content





