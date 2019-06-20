import csv
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from base.consts import INSTANCE_PER_PAGE
from base.forms import SignupForm
from base.models import Product, ProductType
from django.core.paginator import Paginator


class AboutView(TemplateView):
    template_name = "about.html"


class ProductView(View):
    def get(self, request, product_id):
        product_ret = get_object_or_404(Product, pk=product_id)
        return render(request, 'product.html', {'product': product_ret})

    def create(self, name, price = 1000, type_p = -1):
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


def signup(request):
    form = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print('Iam here!')
            form.save()
            return HttpResponse("Member is Created!")
    else:
        form = SignupForm()
    return render(request, 'signup_form.html', {'form': form})


def signup_success(request):
    return render(request, 'success.html')


