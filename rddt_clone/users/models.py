from django.contrib.auth.models import AbstractUser
from django.db import models
from sorl.thumbnail import ImageField


class GenderChoices:
    """
    Пол
    """
    male = 'male'
    female = 'female'

    CHOICES = (
            (male, "мужской"),
            (female, "женский"),
        )


class User(AbstractUser):
    """
    Модель пользователя
    """
    gender = models.CharField(max_length=128, choices=GenderChoices.CHOICES)
    inn = models.PositiveIntegerField(null=True, blank=True)
    image = ImageField(default='default.png', upload_to='profile_pics')
    about_myself = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.username)
