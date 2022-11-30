from django.shortcuts import render
from .models import Project
from user.models import User

def haha(request,Project_id):
    Project_id=1
    project=Project.objects.get(pk=Project_id)
    user=User.objects.get(pk=3)
    return render(request, 'Projectviews.html',{"p":project,"u":user})