from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "index"),
    # path('planet', views.planet, name = "planet"),
    # path('planet/data', views.data, name = "data"),
    # path('planet/'),
   #  path('producto', views.producto, name = "producto"),
]