from django.contrib import admin
from django.urls import include, path
from Votingresult import views

urlpatterns = [
    path('', views.home, name='home')
]