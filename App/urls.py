from django.urls import path
from App import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('Emprendimiento', views.emprendimiento, name="Emprendimiento"),
    path('Empleados', views.empleados, name="Empleados"),
    path('Proveedores', views.proveedores, name="Proveedores"),
    path('Clientes', views.clientes, name="Clientes"),
    path('buscar/', views.buscar),
]