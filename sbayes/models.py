from django.db import models

class Bayes(models.Model):
    """ Spambayes training storage used to score new messages. """
    word = models.CharField(default='', primary_key=True, max_length=100)
    nspam = models.IntegerField(default=0, null=False)
    nham = models.IntegerField(default=0, null=False)

    def __unicode__(self):
        return self.word
