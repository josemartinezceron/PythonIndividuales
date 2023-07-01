from django.shortcuts import render
from .forms import TaskForm

# Create your views here.
def home(request):
    return render(request, 'home.html' )

def task(request):
    return render(request, 'task.html', {'form':TaskForm})
