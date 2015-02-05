import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_header = models.CharField(max_length=200)
    post_date = models.DateTimeField('date published')
    post_content = models.TextField()

    def __str__(self):
        return self.post_content

    def was_published_recently(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'