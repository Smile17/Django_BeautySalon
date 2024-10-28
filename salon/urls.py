from django.urls import path
from salon import views

urlpatterns = [
    path('', views.index, name='home'),
    path('masters', views.masters, name='masters'),
    path('master/<int:master_id>', views.master, name='master'),
    path('prices', views.prices, name='prices'),
    path('contacts', views.contacts, name='contacts'),
]