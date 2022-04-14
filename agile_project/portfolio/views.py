from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import Portfolio
from agile_project.settings import MEDIA_URL
import os
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    context = {}
    usr = request.user

    try:
        user_avatar = Portfolio.objects.get(full_name=usr)
        context['avatar'] = os.path.join(MEDIA_URL, f'{user_avatar.photo}')
    except:
        context['avatar'] = os.path.join(MEDIA_URL, "person_logo.png")

    context['logo'] = os.path.join(MEDIA_URL, "logo.png")

    return render(request, 'portfolio/index.html', context=context)


@login_required
def profile(request, pk):
    return render(request, 'portfolio/profile.html')


def registration(request):
    context = {}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            # автоматическая авторизация пользователя
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )

            login(request, new_user)
            return redirect('portfolio:index')
    else:
        form = UserCreationForm()

    context['form'] = form
    return render(request, 'registration/registration.html', context=context)
