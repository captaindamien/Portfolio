from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404

import os

from .models import Portfolio
from agile_project.settings import MEDIA_URL
from agile_project.forms import PortfolioForm

def get_person_logo(request):
    user = request.user
    if request.user.is_authenticated and not request.user.is_staff:
        user_avatar = get_object_or_404(Portfolio, username=user)
        if user_avatar.photo:
            return os.path.join(MEDIA_URL, f'{user_avatar.photo}')
        else:
            return os.path.join(MEDIA_URL, 'default_person_logo.png')
    if request.user.is_staff:
        return os.path.join(MEDIA_URL, 'admin_logo.jpg')

def index(request):
    context = {}
    context['avatar'] = get_person_logo(request)
    context['logo'] = os.path.join(MEDIA_URL, "logo.png")

    return render(request, 'portfolio/index.html', context=context)


@login_required
def profile(request, username):
    context = {}
    user = request.user
    context['avatar'] = get_person_logo(request)
    
    # если находит портфолио для юзера
    try:
        user_info = Portfolio.objects.get(username=user)

        context['user_info'] = user_info
        return render(request, 'portfolio/profile.html', context)
    # # если портфолио нет, переходим к созданию/редактированию
    except Exception as e:
        return redirect('portfolio:index')


@login_required()
def edit(request, username):
    context = {}
    context['avatar'] = get_person_logo(request)
    user = request.user
    portfolio = Portfolio.objects.get(username=user)

    if request.method == 'POST':
        # передача данных из формы в модель
        print('hui')
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            print(1)
            form.save()
            print(2)
            return profile(request, username)
    else:
        print(3)
        form = PortfolioForm(instance=portfolio)
    
    context['form'] = form
    context['portfolio'] = portfolio
    return render(request, 'portfolio/edit.html', context=context)


def registration(request):
    context = {}
    context['logo'] = os.path.join(MEDIA_URL, "logo.png")

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

            # автоматическое создание портфолио пользователю
            new_portfolio = Portfolio.objects.create(
                username=request.user
            )

            return profile(request, request.user)
    else:
        form = UserCreationForm()

    context['form'] = form
    return render(request, 'registration/registration.html', context=context)
