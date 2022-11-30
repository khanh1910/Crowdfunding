from django.urls import path
from . import views

urlpatterns = [
    path('Project_<int:Project_id>/', views.haha, name='hoho'),
    path('fund/', views.fund, name='hoho1'),
]