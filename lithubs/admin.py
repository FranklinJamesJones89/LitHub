from django.contrib import admin

from . models import Repository, Room, Message, Topic

# Register your models here.

admin.site.register(Repository)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
