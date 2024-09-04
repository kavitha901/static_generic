from django.urls import path
from travel.views import *
app_name='ootyhills'
urlpatterns=[
    path('ooty/',ooty,name='ooty')
]