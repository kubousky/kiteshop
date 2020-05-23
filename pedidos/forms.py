from django import forms
from .models import Pedido


class FormularioDePedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'apellido', 'email', 'direccion',
                'codigo_postal', 'ciudad']