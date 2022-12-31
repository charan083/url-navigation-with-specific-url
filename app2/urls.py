from django.urls import path
from app2.views import *
app_name='prakashraj'

urlpatterns=[
    path('temper1/',temper1,name='temper1')
    
]