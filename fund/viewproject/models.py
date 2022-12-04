import datetime
from django.db import models
from user.models import User
import os

class Project(models.Model):
    Title=models.CharField(max_length=50)
    ShortDescribe=models.CharField(default='',max_length=400)
    Content=models.CharField(default='',max_length=200)
    Owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Category_Choices=[
        ('CN','Công nghệ'),
        ('Dịch Vụ','Dịch vụ'),
        ('DL','Du lịch'),
        ('NN','Nông nghiệp'),
        ('GD','Giáo dục'),
    ]
    Category=models.CharField(default='',choices=Category_Choices,max_length=20)
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
    Funded_Project=models.ForeignKey(Project,on_delete=models.CASCADE,default=0)
    Funded_Money=models.IntegerField(default=0)
