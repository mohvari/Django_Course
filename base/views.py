import csv
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from base.models import Product


class AboutView(TemplateView):
    template_name = "about.html"


class ProductView(View):
    def get(self, request, product_id):
        product_ret = get_object_or_404(Product, pk=product_id)
        return render(request, 'product.html', {'product': product_ret})


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
    current_time = datetime.now()
    return render(request, "home.html", {'current_time': current_time})
