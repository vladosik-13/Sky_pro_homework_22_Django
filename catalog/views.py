from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")


def product_list(request):
    products = Product.objects.all()
    context = {"products":  products}
    return render(request, "catalog/product_list.html", context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_details.html", context)
