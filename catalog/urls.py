from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import ProductListView, ProductDetailView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name="product_detail"),
    path('catalog/create', ProductCreateView.as_view(), name="product_create"),
]
