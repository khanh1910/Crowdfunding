from django.urls import path
from . import views

urlpatterns = [
    path('', views.listnews, name="list_news"),
]