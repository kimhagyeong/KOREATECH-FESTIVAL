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
    path('board/', include('board_main.urls')),
    path('board/<int:board_id>', board_detail.views.detail, name='detail'),
    path('board/detail/<int:board_id>/create/comment',board_detail.views.createcomment, name="createcomment"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    