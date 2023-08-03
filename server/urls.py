from django.urls import re_path
from .views import login , signup

urlpatterns = [
    re_path('login',login),
    re_path('signup',signup)
]
