from django.urls import path
from food.views import *
app_name='foodies'
urlpatterns=[
    path('biriyani/',biriyani,name='biriyani')
]