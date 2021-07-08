from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from .serializers import ProductoSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_productos(request):
    
    '''
    LISTA TODOS LOS PRODUCTO
    '''
    if (request.method=='GET'):
        productos=Producto.objects.all()
        serializer=ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif (request.method=='POST'):
        print(request)
        data=JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view (['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))    
def detalle_producto(request, id):
    
    """
    GET, UPDATE O DELETE DE UN PRODUCTO EN PARTICULAR
    """   
    try:
        productos = Producto.objects.get(cod_producto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductoSerializer(productos)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(productos, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
    elif request.method == 'DELETE':
        productos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

         
   
    
       





