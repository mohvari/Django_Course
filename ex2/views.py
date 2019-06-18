from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
from ex2.models import ExProduct


def add_product(request, in_product_name, in_product_price):
    ExProduct.objects.create(name=in_product_name, price=in_product_price)
    pro = ExProduct.objects.get(name=in_product_name, price=in_product_price)
    return json_product(pro)


def json_product(response):
    response = JsonResponse({"id": response.id, "name": response.name, "price": response.price})
    return HttpResponse(response.content)


