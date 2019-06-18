from django.db import models


class ExProduct(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)

