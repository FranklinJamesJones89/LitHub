from django.urls import path

from . import views

app_name = 'lithubs'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signin', views.login_page, name = 'signin'),
    path('signout', views.logout_user, name = 'signout')
]
