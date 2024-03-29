from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

import os

from .models import Portfolio, Feedback
from agile_project.settings import MEDIA_URL
from agile_project.forms import PortfolioForm, FeedbackForm
from django.contrib.auth.models import User


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


def feedback(request):
    form = FeedbackForm(request.POST, request.FILES)
    context = {}
    context = {
            'avatar': get_person_logo(request),
            'logo': os.path.join(MEDIA_URL, "logo.png")
        }
    if request.method == 'POST':
        # передача данных из формы в модель
        if form.is_valid():
            form.save()
            return render(request, 'portfolio/index.html', context=context)
        else:
            form = PortfolioForm(instance=portfolio)
    context['feed_back'] = form
    return render(request, 'portfolio/feedback.html', context=context)


def index(request):
    context = {
        'avatar': get_person_logo(request),
        'logo': os.path.join(MEDIA_URL, "logo.png")
    }

    return render(request, 'portfolio/index.html', context=context)


@login_required
def profile(request, username):
    user = request.user
    context = {'avatar': get_person_logo(request)}

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
    context = {'avatar': get_person_logo(request)}
    user = request.user
    portfolio = Portfolio.objects.get(username=user)

    if request.method == 'POST':
        # передача данных из формы в модель
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return profile(request, username)
    else:
        form = PortfolioForm(instance=portfolio)

    context['form'] = form
    context['portfolio'] = portfolio
    return render(request, 'portfolio/edit.html', context=context)


def user_page(request, username):
    context = {}
    
    user = User.objects.get(username=username)
    user_info = Portfolio.objects.get(username=user)

    context['user'] = user
    context['avatar'] = get_person_logo(request)
    context['portfolio'] = user_info
    context['links'] = user_info.project_links.split(',')
    context['skills'] = user_info.skills.split(',')

    return render(request, f'portfolio/user_pages/user_page_{user_info.template}.html', context=context)


def registration(request):
    context = {'logo': os.path.join(MEDIA_URL, "logo.png")}
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
        print(form)

    context['form'] = form
    return render(request, 'registration/registration.html', context=context)
