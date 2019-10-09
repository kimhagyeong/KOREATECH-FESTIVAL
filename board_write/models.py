from django.db import models

# Create your models here.
class Board_write(models.Model) :
    title = models.CharField(max_length=200)
    date = models.DateTimeCheckMixin(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)