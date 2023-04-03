from django.shortcuts import render
from .models import User

# Create your views here.

def index(request):
    user = User.objects.all()
    
    context = {'user': user}

    return render(request, 'lithubs/index.html', context)
