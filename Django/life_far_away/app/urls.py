from django.urls import path
from . import views
urlspatters = [
    path('', views.index, name='index'),
   # path('planet/', views.planet, name='planet'),
]
