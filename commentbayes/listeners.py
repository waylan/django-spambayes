from djangobayes.filter import filter, build_msg
from django.contrib.comments.models import CommentFlag

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


def make_msg(comment, request):
    """ Return a message from a comment & request. """

    return build_msg(comment.comment,
            author_ip = request.META.get('REMOTE_ADDR', ''),
            author_agent = request.META.get('HTTP_USER_AGENT', ''),
            referer = request.META.get('HTTP_REFERER', ''),
            author = comment.user_name
        )


def on_comment_was_posted(sender, comment, request, **kwargs):
    """ Filter comment. """
    
    try:
        score = filter.score(make_msg(comment, request))
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


def on_comment_was_flagged(sender, comment, flag, created, request, **kwargs):
    """ Train with comment. """

    # Only train once
    if created:
        if flag.flag == CommentFlag.MODERATOR_APPROVAL:
            # Train ham
            filter.train(make_msg(comment, request), False)
            filter.store()
        elif flag.flag == CommentFlag.MODERATOR_DELETION:
            # Train spam
            filter.train(make_msg(comment, request), True)
            filter.store()
