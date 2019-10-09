from django.shortcuts import render, get_object_or_404, redirect
from board_write.models import Board
from board_detail.models import Comment

# Create your views here.

def detail(request, board_id):
    comment = Comment.objects.filter(post=board_id)
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board' : board_detail, 'comment' : comment})

def createcomment(request, board_id):
        #board = get_object_or_404(Board, pk=board_id) #게시글들에서 하나 뽑음

        comments = Comment()
        comments.author = request.POST['author']
        comments.text = request.POST['text']
        comments.post = board_id
        comments.save()

        return redirect('detail', board_id)