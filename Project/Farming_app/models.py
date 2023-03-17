from django.db import models
from datetime import datetime

# Create your models here.

class signup_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    authorised = models.CharField(max_length=10)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    username = models.EmailField()
    password = models.CharField(max_length=12)
    number = models.BigIntegerField()
    city = models.CharField(max_length=15)
    state =models.CharField(max_length=15)
    pincode = models.IntegerField()

class retailer_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    option = models.CharField(max_length=15)
    crop_name =models.CharField(max_length=50)
    crop_about = models.CharField(max_length=150)
    crop_file = models.FileField(upload_to='static/upload',blank=True)
    crop_quantity = models.IntegerField()
    confirmation = models.CharField(max_length=15,blank=True)

class farmercomplain_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField()
    complaint_title = models.CharField(max_length=50)
    complaint = models.TextField()
    number = models.BigIntegerField()
    state =models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    confirmation = models.CharField(max_length=15,default='unread',blank=True)

class farmertips_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    subject = models.CharField(max_length=50)
    tips = models.CharField(max_length=200)

class feedback_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    subject = models.CharField(max_length=50)
    feedback = models.CharField(max_length=200)

class contactus_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    message = models.TextField()