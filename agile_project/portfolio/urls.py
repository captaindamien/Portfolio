from django.urls import path
from .views import index, registration, login

app_name = 'portfolio'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', index),
    path('login', login, name="login"),
    path('registration', registration, name="registration"),
]
