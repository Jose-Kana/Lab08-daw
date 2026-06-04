from rest_framework import serializers
from .models import Categoria, Producto, Pedido, DetallePedido, Direccion

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

# --- SERIALIZADORES CON JSON ANIDADOS (Requisito de la práctica) ---

class CategoriaSerializer(serializers.ModelSerializer):
    # Anidamos los productos. 'producto_set' busca todos los productos de esta categoría.
    productos = ProductoSerializer(many=True, read_only=True, source='producto_set')

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'productos']

class PedidoSerializer(serializers.ModelSerializer):
    # Anidamos los detalles del pedido para que la consulta sea compleja y completa.
    detalles = DetallePedidoSerializer(many=True, read_only=True, source='detallepedido_set')

    class Meta:
        model = Pedido
        fields = ['id', 'usuario', 'fecha', 'estado', 'total', 'detalles']