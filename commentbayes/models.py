from django.contrib.comments.signals import comment_was_posted
from commentbayes.signals import on_comment_was_posted

# Connect to signals
comment_was_posted.connect(on_comment_was_posted)

# No models here.

