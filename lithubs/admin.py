from django.contrib import admin
from .models import User, Repository, LikeRepository

# Register your models here.

admin.site.register(User)
admin.site.register(Repository)
admin.site.register(LikeRepository)
