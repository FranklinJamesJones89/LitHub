from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Repository
from .forms import RepositoryForm

import random

# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def profile(request):
    repositories = Repository.objects.order_by('created')
    repo_length = Repository.objects.all()
    contributions = len(repo_length)
    context = {'repositories': repositories[:6], 'contributions': contributions}
    return render(request, 'lithubs/profile.html', context)

def repositories(request, username):
    repositories = Repository.objects.order_by('created')
    context = {'repositories': repositories}
    return render(request, 'lithubs/repositories.html', context)

def repository(request, repository_id):
    repository = Repository.objects.get(id = repository_id)
    entries = repository.entry_set.order_by('-created')
    context = {'repository': repository, 'entries': entries}
    return render(request, 'lithubs/repository.html', context)

@login_required
def new_repository(request):
    # Add a new repository
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = RepositoryForm()
    else:
        # POST data submittted; process data
        form = RepositoryForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('lithubs:repositories')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'lithubs/new_repository.html', context)


