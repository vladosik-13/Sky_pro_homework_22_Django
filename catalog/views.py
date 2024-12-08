from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, "catalog/home.html")


def contacts(request):
    return render(request, "catalog/contacts.html")


def product_list(request):
    products = Product.objects.all()
    context = {"products":ех  products}
    return render(request, "catalog/base.html", context)
