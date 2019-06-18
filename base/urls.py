from . import views
from django.urls import path

urlpatterns = [
    # path('/', views.AboutView.as_view, name='about-us'),
    path('about/', views.AboutView.as_view(), name='about-us'),
    path('report/', views.report, name='report'),
]
