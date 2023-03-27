from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import decorators
from django.contrib import messages
from .forms import MyUserCreationForm
from .models import User

# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def login_page(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('lithubs:feed')

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
            return redirect('lithubs:feed')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page': page}

    return render(request, 'lithubs/components/forms/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('lithubs:index')

def register(request):
    form = MyUserCreationForm
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            
            return redirect('lithubs:index')
        else:
            messages.error(request, 'Error during registration')

    return render(request, 'lithubs/components/forms/login_register.html')

def feed(request):
    context = {}
    return render(request, 'lithubs/feed.html', context)
