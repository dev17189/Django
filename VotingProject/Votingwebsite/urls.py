from django.contrib import admin
from django.urls import include, path
from Votingwebsite import views

urlpatterns = [
    path('', views.home, name='home')
]