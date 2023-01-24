from rest_framework import serializers

from api import models


class ProductsSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    price = serializers.CharField(max_length=30)
    description = serializers.CharField()
    coint = serializers.IntegerField()
    is_acitive = serializers.BooleanField()


class CategorySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
