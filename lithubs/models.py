from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Repository(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    synopsis = models.TextField()
    genre = models.CharField(max_length = 200)
    form = models.CharField(max_length = 200)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'repositories'

    def __str__(self):
        return self.title
