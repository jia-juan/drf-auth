# -*- coding: utf-8 -*-
from django.urls import path

from .views import profile, login_view, refresh_token_view

urlpatterns = [
    path('profile', profile, name='profile'),  # 測試用view
    path('login', login_view, name='login'),  # login view
    path('refresh-token', refresh_token_view, name='refresh-token'),  # refresh token view
]
