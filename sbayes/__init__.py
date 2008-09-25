try:
    from sbayes.models import Bayes
except:
    # FIXME: this doesn't catch the error on syncdb. I had to comment out 
    # all lines for syncdb to work.

    # DB not yet synced??
    pass
else:
    from sbayes.util import DjangoClassifier
    from spambayes.hammie import Hammie

    db = DjangoClassifier(Bayes)
    filter = Hammie(db)
