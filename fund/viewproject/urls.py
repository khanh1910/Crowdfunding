from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('search/',views.search,name="search"),
    path('success_projects/', views.success_p, name="success_p"),
    path('category_<str:cate>/',views.CatePageHome,name='cate'),
    path('Project_<int:Project_id>/', views.viewproject, name='view'),
    path('Project_<int:Project_id>/fund/', views.xacnhan, name='fund'),
    path('Project_<int:Project_id>/fund/Success', views.XacNhan, name='XN'),
]

