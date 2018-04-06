from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from shopping.models import Product, ProductType
# Create your views here.

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product


