from django.urls import path
from app1.views import *
app_name='ntr1'

urlpatterns=[
    path('temper/',temper,name='temper')
]