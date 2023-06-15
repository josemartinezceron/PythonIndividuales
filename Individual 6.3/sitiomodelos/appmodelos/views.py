from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def usuarios(request):
    users = User.objects.all()
    context = {
        'usuarios':users,

    }
    return render(request, 'usuarios.html',context=context)

def home(request):
    return render(request, 'index.html')