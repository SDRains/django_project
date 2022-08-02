from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
