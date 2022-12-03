from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from user.models import User
from viewproject.models import FundProject, Project
from django.db.models import Count
from django.contrib.auth import authenticate


# Create your views here.
def t1(request, User_id):
   user = User.objects.get(pk=User_id)
   pc = FundProject.objects.annotate(Count("Funded_Project"))
   pc2 = str(user.fundproject_set.all().count())
   list_funded = user.fundproject_set.all()
   list_project = user.project_set.all()
   balance = user.User_Money
   name = user.first_name + " " + user.last_name
   email = user.email
   phone = user.User_Phone
   success_project = 0
   sum = 0
   rec_money = 0
   for obj in list_funded:
        sum = sum + obj.Funded_Money
   for obj in list_project:
        if obj.Project_IsSuccessfull:
            success_project += 1
            rec_money = rec_money + obj.Project_RecentFund
   pc3 = str(user.project_set.all().count())
   curent_user = request.user
   pc10 = curent_user.id
    
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

def update(request, id):
  mymember = User.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


       
