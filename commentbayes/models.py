#from django.contrib.comments.signals import comment_was_posted, \
#                                            comment_was_flagged
from django.db import models
from django.contrib.comments.models import Comment
from commentbayes.util import get_mark

class ScoredComment(Comment):
    """ Track spam filtering/training of comments. """
    score = models.FloatField(blank=True, null=True)
    trained_as = models.CharField(max_length=4, blank=True, null=True)

    @property
    def is_trained(self):
        """ Return True if object has been trained. """
        return bool(self.trained_as)

    def scored_as(self):
        """ Return spam staus as string based on score only. """
        return get_mark(self.score) 

    def status(self):
        """ Return spam status as string based on training or score. """
        if self.is_trained:
            return self.trained_as
        return self.scored_as()

    @property
    def is_spam(self):
        return self.status().lower() == 'spam'

    @property
    def is_ham(self):
        return self.status().lower() == 'ham'
