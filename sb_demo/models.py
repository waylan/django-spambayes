from django.db import models

MARK_CHOICES = (
    ('unsure', 'unsure'),
    ('ham', 'ham'),
    ('spam', 'spam'),
)

TRAIN_CHOICES = (
    ('', ''),
    ('ham', 'ham'),
    ('spam', 'spam'),
)


class Comment(models.Model):
    author = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    mark = models.CharField(max_length=6, choices=MARK_CHOICES)
    score = models.FloatField(null=True, blank=True)
    trained_as = models.CharField(max_length=4, blank=True, default='', \
                                 choices=TRAIN_CHOICES)

    class Meta:
        ordering = ['date']

    def is_trained(self):
        if self.trained_as == 'ham' or self.trained_as == 'spam':
            return True
        return False

