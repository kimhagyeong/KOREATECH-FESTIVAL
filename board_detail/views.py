from django.shortcuts import render

# Create your views here.

def detail(request, board_id):
    return render(request, 'detail.html')