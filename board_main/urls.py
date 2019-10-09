from django.urls import path, include
import board_main.views

urlpatterns = [
    path('', board_main.views.board, name='board'),
    path('new/',include('board_write.urls')),
    
]