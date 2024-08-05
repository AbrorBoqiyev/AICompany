from django.urls import path
from .views import *

urlpatterns = [
    path('', myapp, name='myapp'),
    path('home', home, name='home'),
]
