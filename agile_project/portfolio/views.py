from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

def login(request):
    return render(request, 'portfolio/login.html')

def registration(request):
    return render(request, 'portfolio/registration.html')