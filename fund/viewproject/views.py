from django.shortcuts import render
from .models import Project

def haha(request,Project_id):
    Project_id=1
    project=Project.objects.get(pk=Project_id)
    return render(request, 'base1.html',{"p":project})