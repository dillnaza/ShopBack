from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api import models, serializers


@api_view(['GET'])
def products(request, *args, **kwargs):
    product = models.Products.objects.all()
    serializer = serializers.ProductsSerializers(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_id(request, *args, **kwargs):
    product = get_object_or_404(models.Products.objects.all(), **kwargs)
    serializer = serializers.ProductsSerializers(product)
    return Response(serializer.data)


@api_view(['GET'])
def categories(request, *args, **kwargs):
    category = models.Categories.objects.all()
    serializer = serializers.CategorySerializers(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_id(request, *args, **kwargs):
    category = get_object_or_404(models.Categories.objects.all(), **kwargs)
    serializer = serializers.CategorySerializers(category)
    return Response(serializer.data)
