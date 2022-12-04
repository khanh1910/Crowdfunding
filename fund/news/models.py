from django.db import models

class News(models.Model):
    News_Title=models.CharField(max_length=100)
    News_Content=models.TextField(default='')
    News_Image=models.ImageField(default='')
