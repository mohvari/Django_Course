from django.urls import path
from . import views

urlpatterns = [
    path('power/<int:input_number>', views.first_task, name='firstTask'),
    path('multiply/<int:first_number>/<int:second_number>', views.second_task, name='secondTask'),
    path('primes/<int:first_number>/<int:second_number>', views.third_task, name='thirdTask'),
    path('max/<int:first_number>/<int:second_number>/<int:third_number>', views.fourth_task, name='fourthTask'),
    path('power/', views.index, name='index'),
]
