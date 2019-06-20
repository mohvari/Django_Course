from django.shortcuts import render, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse

from base.models import Product
from ex2.models import ExProduct


def add_product(request, in_product_name, in_product_price):
    ExProduct.objects.create(name=in_product_name, price=in_product_price)
    product = ExProduct.objects.get(name=in_product_name, price=in_product_price)
    return product.get_product()


def find_product(request, product_id):
    product = get_object_or_404(ExProduct, pk=product_id)
    return product.get_product()


