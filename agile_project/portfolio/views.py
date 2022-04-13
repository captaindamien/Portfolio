from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'portfolio/index.html')


def profile(request, pk):
    return render(request, 'portfolio/profile.html')
