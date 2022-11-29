from django.urls import path
from . import views

urlpatterns = [
    path('Project_<int:Project_id>/', views.haha, name='hoho'),
    path('Project_<int:Project_id>/fund/', views.haha, name='hoho'),
]