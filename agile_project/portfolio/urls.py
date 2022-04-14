from django.urls import path, include
from .views import index, profile, registration

app_name = 'portfolio'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', index, name="index"),
    path('profile/<int:pk>', profile, name="profile"),
    path('registration/', registration, name='registration')
]
