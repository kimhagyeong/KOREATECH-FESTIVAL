from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
    path('', main.views.main, name='main'),
]
