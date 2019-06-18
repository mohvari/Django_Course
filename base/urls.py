from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.AboutView.as_view(), name='about-us'),
    path('report/', views.report, name='report'),
    path('base_product/<int:product_id>/', views.ProductView.as_view(), name="product-base-show"),
]
