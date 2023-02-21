from django.urls import path

from . import views

app_name = 'lithubs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('profile/', views.profile, name = 'profile'),
    path('repositories/', views.repositories, name = 'repositories'),
    path('repositories/<int:repository_id>', views.repository, name = 'repository'),
    path('new_repository/', views.new_repository, name = 'new_repository'),
    #path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry')
]
