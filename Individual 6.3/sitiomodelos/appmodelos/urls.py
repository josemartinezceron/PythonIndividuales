
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appmodelos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.usuarios, name='usuarios'), 
]


