from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    User_Money=models.IntegerField(default=0)
    User_Image=models.ImageField(default="/static/images/default_avatar.jpg")
    User_Phone=models.CharField(default='',max_length=15)

