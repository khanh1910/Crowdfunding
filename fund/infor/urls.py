from django.urls import path
from . import views

urlpatterns = [
   path('', views.t1, name='t1'),
   path('test/', views.t1, name='t1'),
]