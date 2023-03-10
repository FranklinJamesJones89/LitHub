from django.forms import ModelForm
from . models import Repository
#from django.contrib.auth.forms import UserCreationForm

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = '__all__'
