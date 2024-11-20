from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='categorias/', verbose_name='Imagen', null=True)

    def __str__(self):
        cadena = "Categoria: " + self.titulo 
        return cadena
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name) #para borrar también la imagen junto al registro
        super().delete()

    
class Videojuego(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT,related_name='get_categorias', null=True) #models.PROTECT es para que proteja al eliminarlo, se pueden también en cascada para borrar un equipo con todo y jugadores
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='videojuegos/', verbose_name='Imagen', null=True)
    descripcion = models.TextField(null=True, verbose_name='Descripcion') # el null es para que sea obligatorio informacion en el campo


    def __str__(self):
        cadena = "Videojuego: " + self.titulo 
        return cadena
    
    def delete(self, using=None, keep_parents=False):
        if self.imagen: # Borra solo la imagen asociada al videojuego
            self.imagen.storage.delete(self.imagen.name) #para borrar también la imagen junto al registro
        super().delete()

    
