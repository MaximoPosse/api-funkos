from django.db import models

class Categoria(models.Model):
    CodigoCategoria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self): 
        return self.Nombre


class Productos(models.Model): 
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Precio = models.FloatField()
    Stock = models.IntegerField()
    Descripcion = models.TextField(max_length=200) 

    Imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )

    Categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='productos'
    )

    def __str__(self):
        return self.Nombre

class FunkoPop(models.Model):
    CodigoFunko = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    SerieAnime = models.CharField(max_length=100)
    Personaje = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=8, decimal_places=2)
    Stock = models.IntegerField()

    def __str__(self):
        return f"{self.Nombre} ({self.SerieAnime})"