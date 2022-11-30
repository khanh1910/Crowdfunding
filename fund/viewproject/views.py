from django.shortcuts import render
from .models import Project
from user.models import User
from django.http import HttpResponse,HttpResponseRedirect

def haha(request,Project_id):
    project=Project.objects.get(pk=Project_id)
    user=User.objects.get(pk=3)
    return render(request, 'Projectviews.html',{"p":project,"u":user})


def e(request,Project_id):
    p=Project.objects.get(pk=Project_id)
    context={
        "p":p,
    }
    return render(request,"thanhtoanContent.html",context)


def fund(request):
    user=request.user
    Project_id=1
    p=Project.objects.get(pk=Project_id)
    if request.method=='POST':
        user.Money-=int(request.POST.get("num"))*p.Price
        p.RecentFund+=int(request.POST.get("num"))*p.Price
        user.save()
        p.save()
    u="/project/Project_"+str(Project_id)
    return HttpResponseRedirect(u)