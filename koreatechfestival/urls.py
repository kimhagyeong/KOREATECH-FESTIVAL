from django.contrib import admin
from django.urls import path, include
import main.views
import board_write.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main.views.home, name = 'home'),
    path('board/new/',board_write.views.new, name='new')
]
