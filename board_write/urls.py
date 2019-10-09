from django.contrib import admin
from django.urls import path, include
import main.views
import board_write.views

urlpatterns = [
    path('',main.views.home, name = 'home'),
    #path('create/', views.createPost, name= 'createPost'),
    
]
