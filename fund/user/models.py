from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    User_Money=models.IntegerField(default=0)
    User_Image=models.ImageField(default='')
    User_Phone=models.CharField(default='',max_length=15)

class Project(models.Model):
    Project_Title=models.CharField(max_length=50)
    Project_Content=models.TextField
    Project_Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Project_Images=models.ImageField
    Project_GoalFund=models.IntegerField
    Project_RecentFund=models.IntegerField
    Project_DateEnd=models.DateTimeField
    Project_IsSuccessfull=models.BooleanField