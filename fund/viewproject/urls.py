from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project_form', views.project_form, name='project_form'),
    path('Project_<int:Project_id>/', views.viewproject, name='view'),
    path('Project_<int:Project_id>/fund/', views.e, name='fund'),
    path('Project_<int:Project_id>/fund/Success', views.XacNhan, name='XN'),
]

