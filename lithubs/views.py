from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . forms import RepositoryForm, MyUserCreationForm, RoomForm, UserForm
from . models import Repository, Room, Topic, Message, User

# Create your views here.

def index(request):
    return render(request, 'lithubs/index.html')

def profile(request, pk):
    user = User.objects.get(id = pk)
    repos = user.repository_set.all()[:6]
    
    context = {'user': user, 'repos': repos}

    return render(request, 'lithubs/profile.html', context)


def login_page(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('lithubs:index')

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

def repository(request, pk):
    repos = Repository.objects.get(id = pk)
    context = {'repos': repos}
    return render(request, 'lithubs/repository.html', context)

def repositories(request, pk):
    user = User.objects.get(id = pk)
    repos = user.repository_set.all()

    context = {'user': user, 'repos': repos}

    return render(request, 'lithubs/profile.html', context)

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
            repository = form.save(commit = False)
            repository.user = request.user
            repository.save()

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


def discussion(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
        )
    
    topics = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains = q))

    context = {'rooms': rooms, 'topics': topics, 'room_messages': room_messages}

    return render(request, 'lithubs/discussion.html', context)

def room(request, pk):
    room = Room.objects.get(id = pk)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
        user = request.user,
        room = room,
        body = request.POST.get('body')
        )
        room.participants.add(request.user)

        return redirect('lithubs:room', pk = room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}

    return render(request, 'lithubs/room.html', context)

@login_required(login_url = 'lithubs:login')
def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name = topic_name)
        
        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )

        return redirect('lithubs:discussion')
    
    return render(request, 'lithubs/room_form.html')

def update_room(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance = room)
    
    context = {'form': form}

    return render(request, 'lithubs/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id = pk)

    if request.user != room.host:
        return HttpResponse('You are not the owner')

    if request.method == 'POST':
        room.delete()

        return redirect('lithubs:discussion')

    return render(request, 'lithubs/delete.html', {'obj' : room})

def delete_message(request, pk):
    message = Message.objects.get(id = pk)

    if request.user != message.user:
        return HttpResponse('You are not the owner')

    if request.method == 'POST':
        message.delete()

        return redirect('lithubs:discussion')

    return render(request, 'lithubs/delete.html', {'obj' : message})

@login_required(login_url = 'lithubs:login')
def update_user(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = user)
        
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('lithubs:profile', pk = user.id)
        else:
            print('invalid form')

    context = {'form': form}

    return render(request, 'lithubs/update-user.html', context)

