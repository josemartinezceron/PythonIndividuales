from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def usuarios(request):
    users = User.objects.all()
    context = {
        'usuarios':users,

    }
    return render(request, 'usuarios.html',context=context)

def home(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('User created successfully')
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Username already exists'})
        return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Password not match'})
