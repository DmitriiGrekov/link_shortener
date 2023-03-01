from django.urls import path, include
from .views import main_page, redirect_user

urlpatterns = [
    path('', main_page),
    path('<str:code>/', redirect_user)
]
