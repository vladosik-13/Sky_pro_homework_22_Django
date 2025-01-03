from django.urls import path
from django.views.generic import DetailView

from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
]
