from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('title', max_length=151, db_index=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return'{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
