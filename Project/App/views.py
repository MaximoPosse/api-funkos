from django.shortcuts import render
from .models import Categoria, Productos, FunkoPop
from .serializers import SerializersCategoria, SerializersProductos, SerializersFunkoPop
from rest_framework import viewsets


def Inicio(request):
    return render(request, 'Base.html')


class ViewProductos(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = SerializersProductos


class ViewCategoria(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = SerializersCategoria


class ViewFunkoPop(viewsets.ModelViewSet):
    queryset = FunkoPop.objects.all()
    serializer_class = SerializersFunkoPop
   