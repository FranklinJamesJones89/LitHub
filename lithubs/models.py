from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique = True)
    bio = models.TextField(null = True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Repository(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    synopsis = models.TextField(max_length = 1000)
    genre = models.CharField(max_length = 200)
    form = models.CharField(max_length = 200) 
    text = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    #avatar = models.ImageField(upload_to = 'uploads/', null = True, blank = True)
    #file = models.FileField(upload_to = 'uploads/', null = True, blank = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'repositories'
        ordering = ['-updated', '-created']

class Room(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    repository = models.ForeignKey(Repository, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length =  200)
    description = models.TextField(null = True, blank = True)
    #participants = 
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.body[:50]
    created = models.DateTimeField(auto_now_add = True)
