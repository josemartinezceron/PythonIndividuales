from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('noticias/', views.noticias, name='noticias'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),   
]
