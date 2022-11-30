from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.t1, name='t1'),
]