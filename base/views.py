import csv
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from base.consts import INSTANCE_PER_PAGE
from base.forms import SignupForm, LoginForm
from base.models import Product, ProductType
from django.core.paginator import Paginator


class AboutView(TemplateView):
    template_name = "about.html"


class ProductView(View):
    def get(self, request, product_id):
        product_ret = get_object_or_404(Product, pk=product_id)
        return render(request, 'product.html', {'product': product_ret})

    def create(self, name, price=1000):
        Product.objects.create(name=name, price=price)


class ProductTypeView(View):
    def get_or_create(self, title):
        if ProductType.objects.filter(title=title):
            return ProductType.objects.filter(title=title)
        return ProductType.objects.create(title=title)


def report(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    writer.writerow(['Hello', 'Here I am'])
    return response


@login_required
def home(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, INSTANCE_PER_PAGE)
    page = request.GET.get('page', 1)
    products_page = paginator.get_page(page)
    current_time = datetime.now()
    return render(request, "home.html", {'current_time': current_time, 'products_page': products_page})


def signup_first(request):
    # request.POST.get('name', 'pass')
    # return render(request, 'signup.html', {})
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            type_p = ProductTypeView.get_or_create(title=form.cleaned_data.get('type'))
            Product.objects.create(name=form.cleaned_data.get('name'),
                                   price=form.cleaned_data.get('price'), type=type_p)
    else:
        form = SignupForm()
    return render(request, 'signup_form.html', {'form': form})


# def signup(request):
#     form = None
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # print('Iam here!')
#             form.save()
#             return redirect(reverse('login-view'))
#     else:
#         form = SignupForm()
#     return render(request, 'signup_form.html', {'form': form})


class SignupView(FormView):
    template_name = 'signup_form.html'
    form_class = SignupForm
    success_url = '/login' # or we can say reverse_lazy('login-view')


def signup_success(request):
    return render(request, 'success.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            password_raw = form.cleaned_data.get('password')
            print(password_raw)
            user = authenticate(username=username, password=password_raw)
            if user is not None:
                login(request, user)
                print(user)
                return redirect(reverse('home'))
            else:
                print(form.errors)
                return redirect(reverse('signup-class-view'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



