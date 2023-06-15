
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appmodelos import views

urlpatterns = [
    path('home/', views.home, name='proyectos'),
    path('users/', views.usuarios, name='usuarios'), 
]


