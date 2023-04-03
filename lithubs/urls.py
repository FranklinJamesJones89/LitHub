from django.urls import path

from . import views

app_name = 'lithubs'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('profile/<str:pk>', views.profile, name = 'profile'),
    path('repository/<str:pk>', views.repository, name = 'repository'),
    path('repository_form', views.repository_form, name = 'repository-form'),
    path('settings', views.settings, name = 'settings'),
    path('signin', views.login_page, name = 'signin'),
    path('signout', views.logout_user, name = 'signout'),
    path('feed', views.feed, name = 'feed'),
    path('register', views.register, name = 'register')
]
