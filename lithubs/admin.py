from django.contrib import admin
from .models import User, Repository, Room, Message

# Register your models here.

admin.site.register(User)
admin.site.register(Repository)
admin.site.register(Room)
admin.site.register(Message)

