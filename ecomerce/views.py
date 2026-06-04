from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Categoria, Producto, Pedido, DetallePedido, Direccion
from .serializers import (
    CategoriaSerializer, 
    ProductoSerializer, 
    PedidoSerializer, 
    DetallePedidoSerializer, 
    DireccionSerializer
)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer