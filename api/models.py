from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s" % self.title


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)
    worklog = models.PositiveSmallIntegerField(default=0)
    status = models.ForeignKey(settings.TASK_STATUS_MODEL)
    parent = models.ForeignKey(settings.TASK_MODEL)


class TaskStatus(models.Model):
    status = models.CharField(max_length=10, unique=True)