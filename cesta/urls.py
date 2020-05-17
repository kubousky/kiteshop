from django.urls import path
from . import views

app_name = 'cesta'

urlpatterns = [
    path('', views.cesta_detalles, name='cesta_detalles'),
    path('anadir/<int:producto_id>/',
        views.cesta_anadir,
        name='cesta_anadir'),
    path('eliminar/<int:producto_id>/',
        views.cesta_eliminar,
        name='cesta_eliminar'),
]