from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
import os
import random
import string
import math

# Create your views here.
def rand_str():
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

def new(request) :
    return render(request,'new.html')

def createPost(request) :
    if request.method == 'POST' :
        boards = Board()

        
        boards.title = request.POST['title']
        boards.body = request.POST['body']

        
        try :
            fileStr = 'file'
            file = request.FILES[fileStr]
            filename = rand_str()+".PNG"

            module_dir = os.path.dirname(__file__)
            upload_path = module_dir.split('\\board_write')
        
            fp = open('%s/%s' % (upload_path[0]+"\\media\\images", filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            boards.image = 'images/'+filename

        except :
            boards.image = 'images/default.png'

    
    else :
        return render(request,'new.html')
    
    boards.save()
    return redirect('/board/' + str(boards.id)) # URL 경로 board로
    
    
