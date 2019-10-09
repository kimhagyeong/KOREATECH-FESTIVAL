from django.urls import path
from . import views

urlpatterns = [
    #path('',main.views.home, name = 'home'),
    path('', views.new, name='new'),
    path('create/', views.createPost, name='createPost'),
]