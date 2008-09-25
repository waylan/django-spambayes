from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from sb_demo.models import Comment
from djangobayes.filter import filter

def index(request):
    """ Display all comments to date. """
    return render_to_response('comments.html', \
                              {'comments': Comment.objects.all(), \
                               'is_staff': request.user.is_staff})

def get_mark(score):
    """ helper method - return mark based on score """
    if score < 0.3:
        return "ham"
    if score > 0.8:
        return "spam"
    return "unsure"

def add_comment(request):
    """ Add and score a Comment. """
    if request.method == "POST":
        try:
            score = filter.score(request.POST['body'])
        except: # ZeroDivisionError, AssertionError:
            score = None
            mark = 'unsure'
        else:
            mark = get_mark(score)
        comment = Comment(author = request.POST['name'], \
                          email = request.POST['email'], \
                          body = request.POST['body'], \
                          score = score, \
                          mark = mark)
        comment.save()
    return HttpResponseRedirect('/sb_demo/')

def train(request):
    """ Train SpamBayes with a specific Comment. """
    if request.method == "POST" and request.user.is_staff:
        is_spam = True
        if request.POST['mark'] == 'ham':
            is_spam = False
        comment = Comment.objects.get(pk=request.POST['comment_id'])
        filter.train(comment.body, is_spam)
        filter.store()
        comment.trained_as = request.POST['mark']
        comment.save()
    return HttpResponseRedirect('/sb_demo/')

