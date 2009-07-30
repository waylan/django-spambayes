"""
commentbayes
============

An add-on to Django's contrib.comments app that adds SpamBayes filtering.
"""

from commentbayes.models import ScoredComment
from commentbayes.forms import ScoredCommentForm

def get_model():
    return ScoredComment

def get_form():
    return ScoredCommentForm
