from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import Portfolio


def index(request):
    content = {}
    usr = request.user
    try:
        user_avatar = Portfolio.objects.get(full_name=usr)
        content['avatar'] = user_avatar.photo
    except:
        content['avatar'] = "../../media/person_logo.png"

    content['logo'] = "../../media/logo.png"
    return render(request, 'portfolio/index.html', content)


def profile(request, pk):
    return render(request, 'portfolio/profile.html')
