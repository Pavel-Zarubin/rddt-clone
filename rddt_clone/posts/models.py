from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('title', max_length=151, db_index=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=160)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content




