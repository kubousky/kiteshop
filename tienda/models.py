from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:                      # contains metadata
        ordering = ('nombre',)       # We say Django to sort results in name field 
        verbose_name = 'categoria'   # A human-readable name for the object, if not class MyCategory -> "my category"
        verbose_name_plural = 'categorias'  # If this isn’t given, Django will use verbose_name + "s". -> "categorys"!

    def __str__(self):
        return self.nombre
    # The convention in Django is to add below method to the model that returns the canonical URL of the object
    def get_absolute_url(self):      #sometimes we have 1 category or product on two diferent pages; This method select a preferred URL - a canonical URL
            return reverse('tienda:producto_lista_por_categoria',   # <- primer parametro: viewname (principal\tienda\urls.py)
                        args=[self.slug])   


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,
                                related_name='productos',
                                on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d',
                            blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nombre',)
        index_together = (('id', 'slug'),) # las peticiones se irá haciendo por 'id' y por 'slug'. Eso mejorará el rendimiendo de las peticiones 

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
            return reverse('tienda:producto_detalles', args=[self.id, self.slug])

