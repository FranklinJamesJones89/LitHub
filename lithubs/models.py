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
    title = models.CharField(max_length = 200, blank = True)
    synopsis = models.TextField(blank = True)
    genre = models.CharField(max_length = 200, blank = True)
    form = models.CharField(max_length = 200, blank = True)
    body = models.TextField(blank = True)
    image = models.ImageField(null = True, default = 'default-repo-image.jpg', blank = True)
    num_of_likes = models.IntegerField(default = 0, null = True, blank = True)
    num_of_comments = models.IntegerField(default = 0, null = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'repositories'
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title

class LikeRepository(models.Model):
    repo_id = models.CharField(max_length = 500)
    username = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = 'likerepositories'

    def __str__(self):
        return self.username

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    repo = models.ForeignKey(Repository, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.body[:50]


