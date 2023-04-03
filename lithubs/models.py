from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique = True)
    bio = models.TextField(null = True)
    avatar = CloudinaryField(default = 'v1680540852/xrl5mtwt3wzqyh992ovs.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


