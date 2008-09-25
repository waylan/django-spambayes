from spambayes.classifier import Classifier
from django.core.exceptions import ObjectDoesNotExist

class DjangoClassifier(Classifier):
    """ 
    SpamBayes Classifier object that wraps the Django db model. 
    
    """

    def __init__(self, Model):
        """ 
        Note that this class is initialized with a 'Django Model' rather than
        a db name. It expects the Model itself, not an instance. Therefore, 
        one needs to do:

            from sbayes.models import Bayes
            db = DjangoClassifier(Bayes)

        """
        Classifier.__init__(self)
        self.statekey = 'save state'
        self.Model = Model
        self.load()

    def load(self):
        try:
            row = self.Model.objects.get(word=self.statekey)
        except ObjectDoesNotExist:
            self.nspam = 0
            self.nham = 0
        else:
            self.nspam = row.nspam
            self.nham = row.nham

    def store(self):
        self._set_row(self.statekey, self.nspam, self.nham)

    def _set_row(self, word, nspam, nham):
        row = self.Model(word=word, nspam=nspam, nham=nham)
        row.save()

    def _wordinfoget(self, word):
        try:
            row = self.Model.objects.get(word=word)
        except ObjectDoesNotExist:
            return self.WordInfoClass()
        else:
            item = self.WordInfoClass()
            item.__setstate__((row.nspam, row.nham))
            return item

    def _wordinfoset(self, word, record):
        self._set_row(word=word, \
                      nspam=record.spamcount, \
                      nham=record.hamcount)

    def _wordinfodel(self, word):
        try:
            row = self.Model.objects.get(word=word)
        except ObjectDoesNotExist:
            pass
        else:
            row.delete()

    def _wordinfokeys(self):
        rows = self.Model.objects.all()
        return [r.word for r in rows]
        return [r['word'] for r in rows]
