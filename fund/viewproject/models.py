import datetime
from django.db import models
from user.models import User
import os

class Project(models.Model):
    Title=models.CharField(max_length=50)
    ShortDescribe=models.TextField(default='',max_length=100)
    Content=models.TextField(default='')
    Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Image=models.ImageField(null=True)
    Image_Content=models.ImageField(null=True,blank=True)
    GoalFund=models.IntegerField(default=0)
    RecentFund=models.IntegerField(default=0)
    DateEnd=models.DateTimeField(auto_now=True)
    IsSuccessfull=models.BooleanField(default=False)
    Location=models.CharField(default='',max_length=50)
    Price=models.IntegerField(default=0)

class FundProject(models.Model):
    Project_Funder=models.ForeignKey(User,on_delete=models.CASCADE)
    Funded_Project=models.ForeignKey(Project,on_delete=models.CASCADE)
    Funded_Money=models.IntegerField(default=0)
