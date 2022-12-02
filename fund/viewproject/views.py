from django.shortcuts import render
from .models import Project,FundProject
from user.models import User
from django.http import HttpResponse
from django.contrib import messages

def viewproject(request,Project_id):
    project=Project.objects.get(pk=Project_id)
    user=request.user
    return render(request, 'Projectviews.html',{"p":project,"u":user})

def projects(request):
    Ps=Project.objects.all()
    return render(request,"projects.html",{"Ps":Ps})

def e(request,Project_id):
    p=Project.objects.get(pk=Project_id)
    context={
        "p":p,
    }
    return render(request,"thanhtoanContent.html",context)

def Them_Su_Gop_Von(p,u,So_tien,list):
    fp=FundProject()
    for obj in list:
        if p==obj.Funded_Project and u==obj.Project_Funder:
            obj.Funded_Money+=So_tien
            
        else:
            fp.Funded_Money=So_tien
            fp.Funded_Project=p
            fp.Project_Funder=u
            fp.save()

def XacNhan(request,Project_id):
    p=Project.objects.get(pk=Project_id)
    user=request.user
    funded_money = int(request.POST.get("num"))*p.Price
    if user.Money>=funded_money:
        user.Money-=funded_money
        p.RecentFund+=funded_money
        user.save()
        p.save()
        listfund=FundProject.objects.all()
        Them_Su_Gop_Von(p,user,funded_money,listfund)
        return render(request,"success.html")
    else:
        return render(request,"failed.html")