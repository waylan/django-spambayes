from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class SpamStatus(models.Model):
    """ Track spam filtering/training of models through generic relations. """
    score = models.FloatField(blank=True, null=True)
    trained_as = models.CharField(max_length=4, blank=True, null=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return '<SpamStatus: %s for %s>'% (self.status(), self.content_object)

    def is_trained(self):
        """ Return True if object has been trained. """
        return bool(self.trained_as)

    def is_spam(self):
        """ Return True if object is spam based on training or score. """
        if self.status() == "SPAM":
            return True
        return False

    def status(self):
        """ Return spam status as string based on training or score. """
        if self.is_trained():
            return self.trained_as
        return self.scored_as()

    def scored_as(self):
        """ Return spam staus as string based on score only. """
        if score < HAM_LEVEL:
            return "HAM"
        if score > SPAM_LEVEL:
            return "SPAM"
        return "UNSURE"
