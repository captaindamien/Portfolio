from django.urls import path, include
from .views import index, profile, registration, edit

app_name = 'portfolio'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', index, name="index"),
    path('profile/<str:username>/', profile, name="profile"),
    path('profile/<str:username>/edit/', edit, name='edit'),
    path('registration/', registration, name='registration')
]
