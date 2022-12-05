from django.shortcuts import render
from .models import News

def listnews(request):
    Ns=News.objects.all()
    return render (request,"newss.html",{"Ns":Ns})