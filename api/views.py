from django.http import JsonResponse
from django.shortcuts import render
from . import models


def products(request):
    products = models.Products.objects.all()
    product = [{'name': p.name} for p in products]
    return JsonResponse(product, safe=False)


def product(request, *args, **kwargs):
    product = models.Products.objects.get(id=int(kwargs['id']))
    product_info = {'name': product.name,
                    'price': product.price,
                    'description': product.description,
                    'count': product.coint}
    return JsonResponse(product_info, safe=False)


def categories(request):
    categories = models.Catrgories.objects.all()
    category = [{'name': c.name} for c in categories]
    return JsonResponse(category, safe=False)


def category(request, *args, **kwargs):
    category = models.Catrgories.objects.get(id=int(kwargs['id']))
    category_info = {'name': category.name}
    return JsonResponse(category_info, safe=False)


def index(request):
    products = models.Products.objects.all()
    product = [{'name': p.name} for p in products]
    return JsonResponse(product, safe=False)
