from django.shortcuts import render, redirect
from . forms import RepositoryForm
from . models import Repository

# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def explore(request):
    repos = Repository.objects.all()
    context = {'repos': repos}
    
    return render(request, 'lithubs/explore.html', context)

def create_repository(request):
    form = RepositoryForm()
    
    if request.method == 'POST':
        form = RepositoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lithubs:index')

    context = {'form': form}
    return render(request, 'lithubs/repository_create_form.html' , context)
