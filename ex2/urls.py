from . import views
from django.urls import path

urlpatterns = [
    path('add/<str:in_product_name>/<int:in_product_price>', views.add_product, name='addProduct'),
]
