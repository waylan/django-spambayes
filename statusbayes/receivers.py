from djangobayes.filter import filter, build_msg
from statusbayes.models import SpamStatus

def make_msg(instance):
    """ Return a mesage from a model instance. """
    return build_msg('', **instance.__dict__)

def filter_on_save(sender, instance, created, **kwargs):
    """ Filter a model instance when created. """
    if created:
        try:
            score = filter.score(make_msg(instance))
        except:
            score = None
        status = SpamStatus(content_object=instance, score=score)
        status.save()

