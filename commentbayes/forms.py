from django import forms
from django.contrib.comments.forms import CommentForm
from commentbayes.models import ScoredComment

class ScoredCommentForm(CommentForm):

    def get_comment_model(self):
        """ Use the custom comment model. """
        return ScoredComment

    #def get_comment_create_data(self):
