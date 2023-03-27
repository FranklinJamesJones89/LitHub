from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import decorators
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('lithubs:index')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, 'No such user')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('lithubs:index')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {}

    return render(request, 'lithubs/components/forms/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('lithubs:index')
