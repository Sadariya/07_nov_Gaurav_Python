from django.contrib import admin
from .models import event_model

# Register your models here.

class event_admin (admin.ModelAdmin):

    list_display = ['event_name','event_time','event_information','comments']

admin.site.register(event_model,event_admin)