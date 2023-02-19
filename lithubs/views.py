from django.shortcuts import render

from .models import Repository

import random

# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def repositories(request):
    repositories = Repository.objects.order_by('created')
    context = {'repositories': repositories}
    return render(request, 'lithubs/repositories.html', context)

def repository(request, repository_id):
    repository = Repository.objects.get(id = repository_id)
    entries = repository.entry_set.order_by('-created')
    context = {'repository': repository, 'entries': entries}
    return render(request, 'lithubs/repository.html', context)


