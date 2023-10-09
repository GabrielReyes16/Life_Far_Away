from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "index"),
    path('planet', views.aplanet, name = "planet"),
    path('planet/data', views.data, name = "data"),
    path('our_exoplanet', views.our_exoplanet, name = "our_exoplanet"),
]