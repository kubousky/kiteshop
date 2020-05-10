from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.producto_lista, name='producto_lista'),
    path('<slug:categoria_slug>/', views.producto_lista, 
        name='producto_lista_por_categoria'),
    path('<int:id>/<slug:slug>/', views.producto_detalles,
        name='producto_detalles'),
]
