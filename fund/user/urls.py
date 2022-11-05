from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create, name='create'),
    path('create/poster', views.poster, name='poster'),
    path('register/', views.registration, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),

]

