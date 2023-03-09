from django.shortcuts import render
from . models import Repository

# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def explore(request):
    repos = Repository.objects.all()
    context = {'repos': repos}
    
    return render(request, 'lithubs/explore.html', context)
