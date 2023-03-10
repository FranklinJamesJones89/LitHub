from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . forms import RepositoryForm, MyUserCreationForm
from . models import Repository

# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def profile(request, pk):
    user = User.objects.get(id = pk)
    repos = user.repository_set.all()
    context = {'user': user, 'repos': repos}

    return render(request, 'lithubs/profile.html', context)

def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('lithubs:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'No such user')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('lithubs:index')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page': page}
    return render(request, 'lithubs/login_register.html', context)

def register(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)

            return redirect('lithubs:index')

        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'lithubs/login_register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('lithubs:index')

def explore(request):
    repos = Repository.objects.all()
    context = {'repos': repos}
    
    return render(request, 'lithubs/explore.html', context)

@login_required(login_url = 'lithubs:login')
def create_repository(request):
    form = RepositoryForm()
    
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lithubs:index')

    context = {'form': form}
    return render(request, 'lithubs/repository_create_form.html' , context)

@login_required(login_url = 'lithubs:login')
def update_repository(request, pk):
    repo = Repository.objects.get(id = pk)
    form = RepositoryForm(instance = repo)

    if request.user != repo.user:
        return HttpResponse('You are not the owner')


    if request.method == 'POST':
        form = RepositoryForm(request.POST, instance = repo)
        
        if form.is_valid():
            form.save()
            return redirect('lithubs:explore')

    context = {'form': form}
    return render(request, 'lithubs/repository_create_form.html', context)

@login_required(login_url = 'lithubs:login')
def delete_repository(request, pk):
    repo = Repository.objects.get(id = pk)
    
    if request.user != repo.user:
        return HttpResponse('You are not the owner')

    if request.method == 'POST':
        repo.delete()
        return redirect('lithubs:index')

    return render(request, 'lithubs/delete.html', {'obj' : repo})


