from django.db import models

# Create your models here.

class Repository(models.Model):
    title = models.CharField(max_length = 200)
    synopsis = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 50)
    text = models.TextField(null = True, blank = True)
    update = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Repositories'
        


