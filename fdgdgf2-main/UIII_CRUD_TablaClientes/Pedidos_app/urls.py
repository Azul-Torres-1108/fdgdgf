from django.urls import path
from Pedidos_app import views  

urlpatterns = [
    path('', views.inicio_vista, name='inicio'),  # La vista principal
    path('registrarPedidos/', views.registrarPedidos, name='registrarPedidos'),
    path('borrarPedidos/<ID_Pedidos>/', views.borrarPedidos, name='borrarPedidos'),
    path('seleccionarPedidos/<ID_Pedidos>/', views.seleccionarPedidos, name='seleccionarPedidos'),
    path('editarPedidos/', views.editarPedidos, name='editarPedidos')
    
]
