from django.forms import ModelForm
from .models import Repository, Room

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = '__all__'

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
