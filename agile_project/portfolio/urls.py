from django.urls import path
from .views import index, profile, registration, edit, user_page, feedback

app_name = 'portfolio'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', index, name="index"),
    path('feedback', feedback, name="feedback"),
    path('profile/<str:username>/', profile, name="profile"),
    path('profile/<str:username>/edit/', edit, name='edit'),
    path('<str:username>/', user_page, name='user_page'),
    path('accounts/registration/', registration, name='registration')
]
