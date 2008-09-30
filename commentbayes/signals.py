from djangobayes.filter import filter, build_msg

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
    if score < HAM_LEVEL:
        return "ham"
    if score > SPAM_LEVEL:
        return "spam"
    return "unsure"

def on_comment_was_posted(sender, comment, request, **kwargs):
    """ Listed for comment signal and filter comment. """
    msg = build_msg(comment.comment,
            author_ip = request.META.get('REMOTE_ADDR', ''),
            author_agent = request.META.get('HTTP_USER_AGENT', ''),
            referer = request.META.get('HTTP_REFERER', ''),
            author = comment.user_name
    )

    try:
        score = filter.score(msg)
    except:
        score = None
        mark = 'unsure'
    else:
        mark = get_mark(score)

    comment.flags.create(
        user = comment.user,
        flag = mark
    )

    if mark != 'ham':
        comment.is_public = False
    if mark == 'spam':
        comment.is_removed = True
    comment.save()

