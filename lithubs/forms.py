from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Repository


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = '__all__'
        exclude = ['owner']
