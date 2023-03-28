from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(unique = True)
    bio = models.TextField(null = True)
    avatar = models.ImageField(null = True, default = 'avatar.svg')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Repository(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    synopsis = models.TextField()
    genre = models.CharField(max_length = 200)
    form = models.CharField(max_length = 200)
    body = models.TextField()
    image = models.ImageField(null = True, default = 'default-repo-image.jpg')
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'repositories'
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
