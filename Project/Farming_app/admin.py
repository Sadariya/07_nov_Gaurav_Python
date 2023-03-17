from django.contrib import admin
from .models import signup_model,retailer_model,farmercomplain_model,farmertips_model,feedback_model

# Register your models here.

class signup_admin (admin.ModelAdmin):

    list_display = ['authorised','firstname','username','password']

class retailer_admin (admin.ModelAdmin):

    list_display = ['confirmation','option','crop_name','crop_about','crop_quantity']

class farmercomplaint_admin (admin.ModelAdmin):

    list_display = ['firstname','complaint_title','complaint','email']

class farmertips_admin (admin.ModelAdmin):

    list_display = ['subject','tips']

    
class feedback_admin (admin.ModelAdmin):

    list_display = ['subject','feedback']


admin.site.register(signup_model,signup_admin)
admin.site.register(retailer_model,retailer_admin)
admin.site.register(farmercomplain_model,farmercomplaint_admin)
admin.site.register(farmertips_model,farmertips_admin)
admin.site.register(feedback_model,feedback_admin)
