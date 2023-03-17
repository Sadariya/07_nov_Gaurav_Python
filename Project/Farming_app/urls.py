from django.contrib import admin
from django.urls import path
from Farming_app import views

urlpatterns = [

    path('',views.index),   
    path('about/',views.about),
    path('contact/',views.contact),
    path('notes/',views.notes,name='notes'),
    path('profile/',views.profile),
    path('logout/',views.userlogout),
    path('forget/',views.forget),


    # Admin-page Urls :- 
    path('adminpage/',views.adminpage),
    path('farmertips/',views.farmertips),
    path('farmerdata/',views.farmerdata),
    path('farmer_accept/',views.farmer_accept),
    path('feedback/',views.feedback),
    path('deleteadmin/<int:id>',views.deleteadmin,name='deleteadmin'),

    # Farmer-page Urls :-
    path('farmerpage/',views.farmerpage),
    path('farmercomplaint/',views.farmercomplaint),
    path('compaint_status/',views.complaint_status),
    path('farming_tips/',views.farming_tips),
    path('Farmer_feedback/',views.Farmer_feedback),


    # Retailer-page Urls :- 
    path('retailerpage/',views.retailerpage),
    path('editpost_delete/',views.editpost_delete),
    path('delete/<int:id>',views.delete,name='delete'),
    path('Dealer_feedback/',views.Dealer_feedback),

]
