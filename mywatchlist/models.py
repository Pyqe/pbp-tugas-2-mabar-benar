from logging.handlers import RotatingFileHandler
from turtle import title
from django.db import models

class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()