from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyUserCreationForm, RepositoryForm
from .models import User, Repository

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
    repos = Repository.objects.all()

    context = {'repos': repos}
    return render(request, 'lithubs/feed.html', context)

@login_required(login_url = 'lithubs:signin')
def repository_form(request):
    form = RepositoryForm()
    
    if request.method == 'POST':
        form = RepositoryForm(request.POST, request.FILES)
        
        if form.is_valid():
            repository = form.save(commit = False)
            repository.owner = request.user
            form.save()

            return redirect('lithubs:feed')
    
    context = {'form': form}
        
    return render(request, 'lithubs/components/forms/repository_form.html', context)

@login_required(login_url = 'lithubs:signin')
def delete_repository(request, pk):
    repo = Repository.objects.get(id = pk)

    if request.user != repo.owner:
        return HttpResponse('You can only delete your own repositories')

    if request.method == 'POST':
        repo.delete()
        
        return redirect('lithubs:feed')

    return render(request, 'lithubs/delete_repository.html', {'obj': repo})

