from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date


class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)
