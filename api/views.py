from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

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


class CategoryView(ViewSet):
    def list(self, request, *args, **kwargs):
        categories = models.Categories.objects.all()
        serializer = serializers.CategorySerializers(categories, many=True)
        return Response(serializer.data)


class CategoryIDView(ViewSet):
    def retrieve(self, request, pk):
        category = get_object_or_404(models.Categories.objects.all(), pk=pk)
        serializer = serializers.CategorySerializers(category)
        return Response(serializer.data)
