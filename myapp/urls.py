from django.urls import path
from .views import *

urlpatterns = [
    path('', myapp, name='myapp'),
    path('about', about, name='about'),
    
]
