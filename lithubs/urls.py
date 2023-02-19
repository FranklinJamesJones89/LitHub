from django.urls import path

from . import views

app_name = 'lithubs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('repositories', views.repositories, name = 'repositories'),
    path('repositories/<int:repository_id>', views.repository, name = 'repository')
]
