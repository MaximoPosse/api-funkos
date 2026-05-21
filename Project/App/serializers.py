from .models import Categoria, Productos, FunkoPop
from rest_framework import serializers


class SerializersProductos(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'


class SerializersCategoria(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class SerializersFunkoPop(serializers.ModelSerializer):
    class Meta:
        model = FunkoPop
        fields = '__all__'  
        
  
    