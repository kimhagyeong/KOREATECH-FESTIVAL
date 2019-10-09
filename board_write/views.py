from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
# Create your views here.

def new(request) :
    return render(request,'new.html')

def createPost(request) :
    return render(request,'new.html')