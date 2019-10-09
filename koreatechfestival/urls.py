from django.contrib import admin
from django.urls import path, include
import main.views
import board_write.views
import board_main.views
import board_detail.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main.views.home, name = 'home'),
    path('board/new/',board_write.views.new, name='new'),
    path('create/', board_write.views.createPost, name= 'createPost'),
    path('board/',board_main.views.board, name='board'),
    path('board/<int:board_id>', board_detail.views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
