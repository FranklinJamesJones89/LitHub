from django.urls import path

from . import views

app_name = 'lithubs'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('repository/<str:pk>/', views.repository, name = 'repository'),
    path('repository-form/', views.repository_form, name = 'repository-form'),
    path('update-repository/<str:pk>/', views.update_repository, name = 'update-repository'),
    path('delete-repository/<str:pk>/', views.delete_repository, name = 'delete-repository'),
    path('explore/', views.explore, name = 'explore')
]
