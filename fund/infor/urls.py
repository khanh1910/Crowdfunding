from django.urls import path
from . import views

urlpatterns = [
   path('', views.t1, name='t1'),
   path('test/', views.update, name='t1'),
   path('User_<int:User_id>/', views.t1, name='t1'),
   path('User_<int:User_id>/updatepass', views.update, name='updatepass'),
]