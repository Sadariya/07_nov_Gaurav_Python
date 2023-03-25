from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path('', views.index),
    path('apiview/', views.apiweb),
    path('get_specific_data/<int:id>/', views.get_specific_data),
    path('adddata/', views.adddata),
    path('deletedata/<int:id>/', views.deletedata),
    path('updatedata/<int:id>/',views.updatedata),
]
