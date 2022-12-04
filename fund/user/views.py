from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import CreateUserForm


def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Tạo tài khoản thành công: '+user)
            return redirect('login')
    return render(request, 'registration.html', context = {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Sai thông tin đăng nhập !')
            return redirect('login')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'index.html')
def create(request):
    return render(request, 'create.html')
def poster(request):
    return render(request, 'poster.html')

