
from django.contrib import admin

from .models import Categoria
from .models import Producto
from .models import Pedido
from .models import DetallePedido
from .models import Direccion


admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Direccion)