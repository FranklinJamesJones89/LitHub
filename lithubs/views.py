from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyUserCreationForm, CommentForm, UserForm, RepositoryForm
from .models import User, Repository, Comment, LikeRepository
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

@login_required(login_url = 'lithubs:signin')
def delete_comment(request, pk):
    comment = Comment.objects.get(id = pk)

    if request.user != comment.owner:
        return HttpResponse(request, 'You are not the owner')

    if request.method == 'POST':
        comment.delete()

        return redirect('lithubs:feed')

    return render(request, 'lithubs/components/forms/delete_comment.html', {'obj': comment })

@login_required(login_url = 'lithubs:signin')
def like_repo(request):
    username = request.user.username
    repo_id = request.GET.get('repo_id')
    repo = Repository.objects.get(id = repo_id)

    like_filter = LikeRepository.objects.filter(repo_id = repo_id, username = username).first()

    if like_filter == None:
        new_like = LikeRepository.objects.create(repo_id = repo_id, username = username)
        new_like.save()
        repo.num_of_likes = repo.num_of_likes + 1
        repo.save()
        
        return redirect('lithubs:feed')
    else:
        like_filter.delete()
        repo.num_of_likes = repo.num_of_likes - 1
        repo.save()

        return redirect('lithubs:feed')
    
@login_required(login_url = 'lithubs:signin')
def delete_repository(request, pk):
    repo = Repository.objects.get(id = pk)

    if request.user != repo.owner:
        return HttpResponse('You can only delete your own repositories')

    if request.method == 'POST':
        repo.delete()

        return redirect('lithubs:feed')

    return render(request, 'lithubs/components/forms/delete_repository.html', {'obj': repo})

@login_required(login_url = 'lithubs:signin')
def update_repository(request, pk):
    repo = Repository.objects.get(id = pk)
    form = RepositoryForm(instance = repo) 
    
    if repo.owner != request.user:
        return HttpResponse('You can only update your own repositories')
    
    if request.method == 'POST':
        form = RepositoryForm(request.POST, request.FILES, instance = repo) 
        
        if form.is_valid():
            form.save()
        
            return redirect('lithubs:feed')

    context = {'form': form}

    return render(request, 'lithubs/components/forms/repository_form.html', context)
