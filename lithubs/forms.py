from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Comment, Repository


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['owner', 'repo']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['owner', 'repo']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'name', 'bio']

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = '__all__'
        exclude = ['owner']