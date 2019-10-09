from django.db import models

# Create your models here.

class Comment(models.Model):
    post = models.IntegerField()                            #댓글 PK
    author = models.CharField(max_length=15)                #작성자
    text = models.TextField()                               #댓글 내용
    created_date = models.DateTimeField(auto_now_add=True)  #작성 일자
    approved_comment = models.BooleanField(default=False)   #승인 여부

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text