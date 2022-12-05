from django.db import models

class News(models.Model):
    Title=models.CharField(max_length=130)
    Content=models.TextField(default='')
    ShortContent=models.TextField(default='')
    Image=models.ImageField(default='')
