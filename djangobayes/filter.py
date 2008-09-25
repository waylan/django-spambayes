from djangobayes.models import Bayes
from djangobayes.util import DjangoClassifier
from spambayes.hammie import Hammie

db = DjangoClassifier(Bayes)
filter = Hammie(db)
