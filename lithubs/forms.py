from django.forms import ModelForm
from . models import Repository
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = '__all__'

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
