from django.contrib import admin
from django.urls import path
from APIapp import views

urlpatterns = [
    path('', views.index),
    path('getall/', views.getall, name='getall'),
    path('savedata/', views.savedata),
    path('delete/', views.delete),
    path('deleteid/<int:id>', views.deleteid),
    path('update/', views.update),
    path('updateid/<int:id>', views.updateid),
]
