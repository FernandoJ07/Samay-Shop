from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('subirProducto/', views.subirProducto, name='subirProducto'),
    path('crearCategoría/', views.crearCategoría, name='crearCategoría'),
    path('detallesProducto/<slug:identificador>/', views.detallesProducto, name='detallesProducto'),
    path('contacto/', views.contacto, name='contacto'),
    path('tienda/', views.tienda, name="tienda"),
    path('editarProdcuto/<slug:identificador>/', views.editarProducto, name='editarProducto'),
    # path('eliminarProducto/<slug:identificador>', views.eliminarProducto, name='eliminarProducto')

    path('carrito/', views.carrito, name='carrito'),
    path('agregar/<slug:identificador>/', views.agregarProducto, name='add'),
    path('eliminar/<slug:identificador>/', views.eliminarProducto, name='delete'),
    path('decrementar/<slug:identificador>/', views.decrementarProducto, name='decrement'),
    path('limpiar/', views.limpiarCarrito, name='clear'),
                            
]