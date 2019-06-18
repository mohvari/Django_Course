from django.contrib.auth.models import AbstractUser
from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=256, verbose_name="عنوان")


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="نام")
    price = models.IntegerField(default=0, verbose_name="قیمت")
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'type')


class Member(AbstractUser):
    pass
