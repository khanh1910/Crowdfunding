from .models import Project,FundProject
from user.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from viewproject.models import Project
from viewproject.forms import ProjectForm

def viewproject(request,Project_id):
    project=Project.objects.get(pk=Project_id)
    user=request.user
    return render(request, 'base1.html',{"p":project,"u":user})

def projects(request):
    Ps=Project.objects.all()
    return render(request,"projects.html",{"Ps":Ps})

def success_p(request):
    Ps=Project.objects.all()
    a=[]
    for item in Ps:
        if item.GoalFund <= item.RecentFund:
            a.append(item)
    return render(request,"success_projects.html",{"sucPs":a})

def xacnhan(request,Project_id):
    p=Project.objects.get(pk=Project_id)
    context={
        "p":p,
    }
    return render(request,"thanhtoanContent.html",context)

def XacNhan(request,Project_id):
    p=Project.objects.get(pk=Project_id)
    user=request.user
    funded_money = int(request.POST['num'])*p.Price
    if user.Money>=funded_money:
        user.Money-=funded_money
        p.RecentFund+=funded_money
        us = User.objects.all()
        for u in us:
            if p.Owner==u:
                u.Money+=funded_money
                u.save()
        user.save()
        p.save()
        listfund=FundProject.objects.all()
        fp=FundProject()
        for obj in listfund:
            if p==obj.Funded_Project and user==obj.Project_Funder:
                obj.Funded_Money+=funded_money
                obj.save()     
            else:
                fp.Funded_Money=funded_money
                fp.Funded_Project=p
                fp.Project_Funder=u
                fp.save()
        return render(request,"success.html")
    else:
        return render(request,"failed.html")

def CATE(i):
        switcher={
                'NN':'NÔNG NGHIỆP',
                'CN':'CÔNG NGHỆ',
                'GD':'GIÁO DỤC',
                'DV':'DỊCH VỤ',
                'DL':'DU LỊCH',
             }
        return switcher.get(i,"Invalid day of week")

def search(request):
    searched=str(request.POST['searched'])
    Ps=Project.objects.all()
    a=[]
    for p in Ps:
        if searched in p.Category:
            a.append(p)
            continue
        if searched in CATE(p.Category):
            a.append(p)
            continue
        if searched in p.Title:
            a.append(p)
            continue
        if searched in p.Owner.username:
            a.append(p)
            continue
        if searched in p.Location:
            a.append(p)
            continue
    context={
        "searched":searched,
        "list":a
    }
    return render(request,"projects_searched.html",context)


def CatePageHome(request,cate):
    Ps=Project.objects.all()
    l=[]
    for p in Ps:
        if(cate==p.Category):
            l.append(p)
    a=CATE(cate)
    context={
        "list_cate_project":l,
        "cate":a
        }
    return render(request,"cate_projects.html",context)

def project_form(request):
    form=ProjectForm()
    if request.method== 'POST':
        form=ProjectForm(request.POST, request.FILES, Owner=request.user,RecentFund=0,IsSuccessfull=False, Category=request.POST['Category'])
        if  form.is_valid():
            form.save()
            messages.success(request, 'Tạo dự án thành công!')
            return redirect('project_form')
        else:
            form=ProjectForm()
    return render(request,"campaign.html", {'form': form})