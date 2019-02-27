from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img= Image.open(self.image.path)

        if img.height > 150 or img.width > 150:
            size = (150,150)
            img.thumbnail(size)
            img.save(self.image.path)