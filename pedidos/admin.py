from django.contrib import admin
from .models import Pedido, PedidoArticulo


class PedidoArticuloEnlinea(admin.TabularInline):
    model = PedidoArticulo
    raw_id_fields = ['producto']

@admin.register(Pedido)
class PedidoLadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'email',
                    'direccion', 'codigo_postal', 'ciudad', 'pagado',
                    'creado', 'actualizado']
    list_filter = ['pagado', 'creado', 'actualizado']
    inlines = [PedidoArticuloEnlinea]
