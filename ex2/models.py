from django.db import models
from django.http import JsonResponse, HttpResponse


class ExProduct(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)

    def get_product(self):
        response = JsonResponse(
            {
                "id": self.id,
                "name": self.name,
                "price": self.price
            })
        return response
