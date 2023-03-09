from django.forms import ModelForm
from . models import Repository

class RepositoryForm(ModelForm):
    class Meta:
        model = Repository
        fields = '__all__'
