from django.urls import path, include
from .views import index, profile_user, profile_user_edit, registration

app_name = 'portfolio'
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', index, name="index"),
    path('profile/<str:username>', profile_user, name="profile_user"),
    path('profile/<str:username>/edit', profile_user_edit, name="profile_user_edit"),
    path('registration/', registration, name='registration')
]
