from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title
