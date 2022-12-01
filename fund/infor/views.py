from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from user.models import User
from viewproject.models import FundProject, Project
from django.db.models import Count



# Create your views here.
def t1(request, User_id):
   user=User.objects.get(pk=User_id)
   pc=FundProject.objects.annotate(Count('Funded_Project'))
   pc2 =str(user.fundproject_set.all().count())
   list_funded = user.fundproject_set.all()
   sum=0
   for obj in list_funded:
      sum = sum + obj.Funded_Money
   pc3 =str(user.project_set.all().count())
   return render(request, "view_info.html", {"u":user, "pc":pc2, "s":sum, "pc3":pc3})
