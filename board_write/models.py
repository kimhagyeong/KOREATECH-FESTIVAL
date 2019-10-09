from django.db import models

# Create your models here.
class Board(models.Model) :
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)