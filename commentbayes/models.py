from django.contrib.comments.signals import comment_was_posted, \
                                            comment_was_flagged
from commentbayes.listeners import on_comment_was_posted, \
                                   on_comment_was_flagged

# Connect to signals
comment_was_posted.connect(on_comment_was_posted)
comment_was_flagged.connect(on_comment_was_flagged)

# No models here.

