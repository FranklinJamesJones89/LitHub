from django.urls import path
from . import views

app_name = 'lithubs'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('explore', views.explore, name = 'explore'),
    path('create-repository', views.create_repository, name = 'create-repository'),
    path('update-repository/<str:pk>/', views.update_repository, name = 'update-repository'),
    path('delete/<str:pk>/', views.delete_repository, name = 'delete-repository')
]
