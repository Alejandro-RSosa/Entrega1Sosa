from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('perros', views.perros, name= "perros"),
    path('gatos', views.gatos, name= "gatos"),
    path('snackys', views.snacks, name= "snacks"),
    path('alta_perro', views.comida_perro, name="alta_perro"),
    path('alta_gato', views.comida_gato, name="alta_gato"),
    path('alta_snacks', views.comida_snacks, name="alta_snacks"),
    path("buscar_comida", views.buscar_comida, name="buscar_comida"),
    path("buscar", views.buscar)
]
