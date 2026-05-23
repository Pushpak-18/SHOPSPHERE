from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('login_/', login_, name='login_'),
    path('profile/', profile, name='profile'),
    path('logout_', logout_, name='logout_'),
    path('reset_password', reset_password, name='reset_password'),
    path('forgot_pass', forgot_pass, name='forgot_pass'),
    path('update_profile', update_profile, name='update_profile')
]