import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(blank=True, default='')
    profile_picture = models.ImageField(upload_to='profile_images', null=True)
    facebook = models.URLField(null=True)
    linkedin = models.URLField(null=True)

    def __str__(self):
        return self.username