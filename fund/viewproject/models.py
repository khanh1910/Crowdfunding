import datetime
from django.db import models
from user.models import User

class Project(models.Model):
    Project_Title=models.CharField(max_length=50)
    Project_ShortDescribe=models.TextField(default='',max_length=100)
    Project_Content=models.TextField(default='')
    Project_Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Project_Images=models.ImageField(default='')
    Project_GoalFund=models.IntegerField(default=0)
    Project_RecentFund=models.IntegerField(default=0)
    Project_DateEnd=models.DateTimeField(auto_now=True)
    Project_IsSuccessfull=models.BooleanField(default=False)
