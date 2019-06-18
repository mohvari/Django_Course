from . import views
from django.urls import path

urlpatterns = [
    path('<str:input_string>', views.first_task, name='str_first'),
    path('<int:leng>/<str:input_string>', views.second_task, name='str_second'),
]
