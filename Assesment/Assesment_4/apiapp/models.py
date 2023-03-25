from django.db import models
from datetime import datetime

# Create your models here.

class event_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    event_name =models.CharField(max_length=100)
    event_time = models.DateField()
    event_information = models.TextField()
    comments = models.TextField()