from djangobayes.filter import build_msg

try:
    from django.conf.settings import HAM_LEVEL
except ImportError:
    HAM_LEVEL = 0.3

try:
    from django.conf.settings import SPAM_LEVEL
except ImportError:
    SPAM_LEVEL = 0.8

def get_mark(score):
    """ Return mark based on score. """
    if score is not None and score < HAM_LEVEL:
        return "ham"
    if score is not None and score > SPAM_LEVEL:
        return "spam"
    return "unsure"

def make_msg(comment, request):
    """ Return a message from a comment & request. """
    return build_msg('',
            user_name = comment.user_name,
            user_email = comment.user_email,
            user_url = comment.user_email,
            comment = comment.comment,
            user_ip = request.META.get('REMOTE_ADDR', ''),
            user_agent = request.META.get('HTTP_USER_AGENT', ''),
            referer = request.META.get('HTTP_REFERER', ''))

