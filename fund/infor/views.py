from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from user.models import User
from viewproject.models import FundProject, Project
from django.db.models import Count
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def t1(request, User_id):
    user = User.objects.get(pk=User_id)
    pc = FundProject.objects.annotate(Count("Funded_Project"))
    pc2 = str(user.fundproject_set.all().count())
    list_funded = user.fundproject_set.all()
    list_project = user.project_set.all()
    balance = user.Money
    name = user.first_name + " " + user.last_name
    email = user.email
    phone = user.Phone
    success_project = 0
    sum = 0
    rec_money = 0
    for obj in list_funded:
        sum = sum + obj.Funded_Money
    for obj in list_project:
        if obj.GoalFund <= obj.RecentFund:
            success_project += 1
            rec_money = rec_money + obj.RecentFund
    pc3 = str(user.project_set.all().count())
    curent_user = request.user
    pc10 = curent_user.id
    pc11 = user.id
    if pc10 == User_id:
        return render(
            request,
            "view_info.html",
            {
                "u": user,
                "pc": pc2,
                "s": sum,
                "pc3": pc3,
                "pc4": success_project,
                "pc5": rec_money,
                "pc6": balance,
                "pc7": name,
                "pc8": email,
                "pc9": phone,
                "pc11": pc11,
            },
        )
    else:
        return render(
            request,
            "view_info2.html",
            {
                "u": user,
                "pc": pc2,
                "s": sum,
                "pc3": pc3,
                "pc4": success_project,
                "pc5": rec_money,
                "pc6": balance,
                "pc7": name,
                "pc8": email,
                "pc9": "*******",
            },
        )


def update(request, User_id):
    curent_user = request.user
    u = User.objects.get(pk=curent_user.id)
    user = User.objects.get(username=u.username)
    data = request.POST["check_pass"]
    newpass = request.POST["new_pass"]
    checknewpass = request.POST["checknew_pass"]
    check = user.check_password(data)
    error = False
    if check:
        if newpass == checknewpass:
            user.set_password(newpass)
            user.save()
            messages.info(request, "Thay đổi mật khẩu thành công!")
            return HttpResponseRedirect("/login")
        else:
            messages.info(request, "Mật khẩu không khớp!")
            return HttpResponseRedirect("/infor/User_" + str(curent_user.id))
    else:
        messages.info(request, "Mật khẩu sai!")
        return HttpResponseRedirect("/infor/User_" + str(curent_user.id))


def money_exc(request, User_id):
    curent_user = request.user
    u = User.objects.get(pk=curent_user.id)
    user = User.objects.get(username=u.username)
    data = request.POST["check_pass"]
    money_ex = request.POST["money_ex"]
    check = user.check_password(data)
    if check:
        user.Money += int(money_ex)
        user.save()
        messages.info(request, "Nạp tiền thành công")
        return HttpResponseRedirect("/infor/User_" + str(curent_user.id))
    else:
        messages.info(request, "Mật khẩu sai!")
        return HttpResponseRedirect("/infor/User_" + str(curent_user.id))