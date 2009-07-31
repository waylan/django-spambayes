from django.contrib import admin
from django.contrib.comments.admin import CommentsAdmin
from django.contrib.comments.models import CommentFlag
from django.contrib.comments import signals
from commentbayes.models import ScoredComment
from commentbayes import get_model
from commentbayes.util import make_msg
from djangobayes.filter import filter

class CommentModerationAdmin(CommentsAdmin):
    list_display = (
        'name', 'content_type', 'object_pk', 'ip_address', 'submit_date', 
        'is_public', 'is_removed', 'score', 'trained_as'
    )
    actions = ['train_as_ham', 'train_as_spam']

    def train_as_ham(self, request, queryset):
        "Train comments as ham and approve for display."
        cnt = 0
        for comment in queryset:
            flag, created = CommentFlag.objects.get_or_create(
                comment = comment,
                user    = request.user,
                flag    = CommentFlag.MODERATOR_APPROVAL
            )

            comment.is_removed = False
            comment.is_public = True
            comment.trained_as = 'ham'
            comment.save()
            filter.train(make_msg(comment, request), False)
            filter.store()

            signals.comment_was_flagged.send(
                sender  = comment.__class__,
                comment = comment,
                flag    = flag,
                created = created,
                request = request
            )
            cnt += 1
        self.message_user(request, '%s successfully trained as ham.' % self._get_message_bit(cnt))

    def train_as_spam(self, request, queryset):
        "Train comments as spam and remove from public display."
        cnt = 0
        for comment in queryset:
            flag, created = CommentFlag.objects.get_or_create(
                comment = comment,
                user    = request.user,
                flag    = CommentFlag.MODERATOR_DELETION
            )

            comment.is_removed = True
            comment.trained_as = 'spam'
            comment.save()
            filter.train(make_msg(comment, request), True)
            filter.store()

            signals.comment_was_flagged.send(
                sender  = comment.__class__,
                comment = comment,
                flag    = flag,
                created = created,
                request = request
            )
            cnt += 1
        self.message_user(request, '%s successfully trained as spam.' % self._get_message_bit(cnt))

    def _get_message_bit(self, rows_updated):
        if rows_updated == 1:
            return '1 comment was'
        else:
            return '%s comments were' % rows_updated

#if get_model() is Comment:
admin.site.register(ScoredComment, CommentModerationAdmin)
