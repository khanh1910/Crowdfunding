from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Money=models.IntegerField(default=0)
    Image=models.ImageField(default="/static/images/default_avatar.jpg")
    Phone=models.CharField(default='',max_length=15)

