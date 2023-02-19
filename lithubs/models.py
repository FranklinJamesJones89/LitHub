from django.db import models

# Create your models here.

class Repository(models.Model):
    title = models.CharField(max_length = 200)
    synopsis = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 50)
    update = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Repositories'

class Entry(models.Model):
    repository = models.ForeignKey(Repository, on_delete = models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.text[:50]}...'
        


