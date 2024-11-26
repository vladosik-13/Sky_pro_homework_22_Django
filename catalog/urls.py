from django.urls import path

from config.urls import urlpatterns
from . import views

urlpatterns = [
    path('home/', views.home(), name="home"),
    path('contacts/', views.contacts(), name="contacts"),
]
