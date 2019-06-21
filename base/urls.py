from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.AboutView.as_view(), name='about-us'),
    path('report/', views.report, name='report'),
    path('base_product/<int:product_id>/', views.ProductView.as_view(), name="product-base-show"),
    path('signup/success.html', views.signup_success, name='signup-success-view'),
    path('signup/', views.SignupView.as_view(), name='signup-class-view'),
    # path('signup/', views.signup, name='signup-view'),
    path('login/', views.login_view, name='login-view'),
    # path('login/', auth_views.LoginView, name='built-in-login'),
    # path('logout/', auth_views.LogoutView, name='built-in-logout'),

]
