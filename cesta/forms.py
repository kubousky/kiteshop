from django import forms


PRODUCTO_CANTIDAD_ELECCION = [(i, str(i)) for i in range(1, 21)]


class AnadirProductoCestaFormulario(forms.Form):
    cantidad = forms.TypedChoiceField(
                                choices=PRODUCTO_CANTIDAD_ELECCION, # permite al usuario elegir la cantidad entre 1 y 20 del mismo producto 
                                coerce=int) # convierte el input en un entero
    actualizacion = forms.BooleanField(
                                required=False,
                                initial=False,    # False: la cantidad se añade a l cantidad existente, True: la cantidad se sustituye con la nueva
                                widget=forms.HiddenInput)