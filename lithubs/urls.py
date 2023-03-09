from django.urls import path
from . import views

app_name = 'lithubs'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('explore', views.explore, name = 'explore'),
    path('create-repository', views.create_repository, name ="create-repository")
]
