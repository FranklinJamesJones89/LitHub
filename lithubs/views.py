from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyUserCreationForm, CommentForm, UserForm
from .models import User, Repository
# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def profile(request, pk):
    user = User.objects.get(id = pk)
    repos = user.repository_set.all()
    public_repos = Repository.objects.all()

    context = {'user': user, 'repos': repos, 'public_repos': public_repos}

    return render(request, 'lithubs/profile.html', context)

def repository(request, pk):
    repo = Repository.objects.get(id = pk)
    repos = Repository.objects.all()
    repo_comments = repo.comment_set.all()
    
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.owner = request.user
            comment.repo = repo
            form.save()
        else:
            print('not valid')

            return redirect('lithubs:profile', id = pk)

    context = {'repo': repo, 'repos': repos, 'repo_comments' : repo_comments, 'form': form}

    return render(request, 'lithubs/repository.html', context)

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


def feed(request):
    repos = Repository.objects.all()

    context = {'repos': repos}

    return render(request, 'lithubs/feed.html', context)


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

def settings(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = user)

        if form.is_valid():
            print('valid')
            form.save()
            
            return redirect('lithubs:profile', pk = user.id)
        else:
            print('not valid')

    context = {'form': form}

    return render(request, 'lithubs/components/forms/settings_form.html', context)