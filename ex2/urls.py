from . import views
from django.urls import path

urlpatterns = [
    path('add/<str:in_product_name>/<int:in_product_price>', views.add_product, name='add-product'),
    path('<int:product_id>', views.find_product, name='find-product'),
]
