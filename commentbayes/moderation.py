from django.contrib.comments.moderation import CommentModerator
from djangobayes.filter import filter
from commentsbayes.util import make_msg

class CommentBayesModerator(CommentModerator):
    """ A comment moderator which uses djangobayes. """
    delete_scored_spam = False

    def allow(comment, content_object, request):
        """ Score comment and act accordingly. """
        allow = super(CommentBayesModerator, self).allow(comment, content_object, request)
        try:
            comment.score = filter.score(make_msg(comment, request))
        except:
            comment.score = None
        
        if self.delete_scored_spam:
            return allow and not comment.is_spam
        else:
            return allow

    def moderate(comment, content_object, request):
        """ Check comment score and act accordingly. """
        moderate = super(CommentBayesModerator, self)moderate(comment, content_object, request)

        return moderate and not comment.is_ham

