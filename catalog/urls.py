from django.urls import path
from . import views
from catalog.views import product_list, product_details


app_name = "catalog"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("", product_list, name="product_list"),
    path('product/<int:pk>/', product_details, name="product_details"),
]
