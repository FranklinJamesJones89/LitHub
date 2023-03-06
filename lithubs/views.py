from django.shortcuts import render, redirect
from .models import User, Repository
from .forms import RepositoryForm

# Create your views here.

def index(request):
    repos = Repository.objects.all()
    context = {'repos': repos}

    return render(request, 'lithubs/index.html', context)

def repository(request, pk):
    repo = Repository.objects.get(id = pk)
    context = {'repo': repo}
    
    return render(request, 'lithubs/repository.html', context)

def repository_form(request):
    form = RepositoryForm()
    
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('lithubs:index')

    context = {'form': form}
    return render(request, 'lithubs/repository_form.html', context)

def update_repository(request, pk):
    repository = Repository.objects.get(id=pk)

    # Prefill the room data with initial = repository as parameter
    form = RepositoryForm(instance = repository)
    
    if request.method == 'POST':
        form = RepositoryForm(request.POST, instance = repository)
        
        if form.is_valid():
            form.save()
            return redirect('lithubs:index')

    context = {'form': form}
    return render(request, 'lithubs/repository_form.html', context)


def explore(request):
    repos = Repository.objects.all()
    context = {'repos': repos}
    return render(request, 'lithubs/explore.html', context)


