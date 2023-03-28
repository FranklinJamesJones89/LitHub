from django.contrib import admin
from .models import User, Repository, LikeRepository, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Repository)
admin.site.register(LikeRepository)
admin.site.register(Comment)
