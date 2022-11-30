from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def t1(request):
    return render(request, "aaa.html")
