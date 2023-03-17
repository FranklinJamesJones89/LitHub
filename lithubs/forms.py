from django.forms import ModelForm
from . models import Repository, Room, User
from django.contrib.auth.forms import UserCreationForm

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = '__all__'
        exclude = ['user']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
