from djangobayes.models import Bayes
from djangobayes.util import DjangoClassifier
from spambayes.hammie import Hammie
from email import message_from_string

db = DjangoClassifier(Bayes)
filter = Hammie(db)

build_msg(body, **kwargs):
    """ Return a e-mail type message from a dict to pass into filter. """
    msg = message_from_string(body)
    for k, v in kwargs.items():
        msg[k] = v
    return m
