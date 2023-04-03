from django.urls import path

from . import views

app_name = 'lithubs'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('profile/<str:pk>', views.profile, name = 'profile'),
    path('repository/<str:pk>', views.repository, name = 'repository'),
    path('repository_form', views.repository_form, name = 'repository-form'),
    path('update_repository/<str:pk>/', views.update_repository, name = 'update-repository'),
    path('delete_repository/<str:pk>/', views.delete_repository, name = 'delete-repository'),
    path('like_repo', views.like_repo, name = 'like-repo'),
    path('settings', views.settings, name = 'settings'),
    path('delete_comment/<str:pk>/', views.delete_comment, name = 'delete-comment'),
    path('signin', views.login_page, name = 'signin'),
    path('signout', views.logout_user, name = 'signout'),
    path('feed', views.feed, name = 'feed'),
    path('register', views.register, name = 'register')
]
