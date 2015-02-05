import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_header = models.CharField(max_length=200)
    post_date = models.DateTimeField('date published')
    post_content = models.TextField()

    def __str__(self):
        return self.post_content

    def wasPublshedRecently(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days=1)