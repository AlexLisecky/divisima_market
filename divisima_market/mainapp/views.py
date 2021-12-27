from django.shortcuts import render
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'mainapp/index.html'
    queryset = []


class ProductView(ListView):
    template_name = 'mainapp/product.html'
    queryset = []


class ContactView(ListView):
    template_name = 'mainapp/contact.html'
    queryset = []


class CheckoutView(ListView):
    template_name = 'mainapp/checkout.html'
    queryset = []


class CategoryView(ListView):
    template_name = 'mainapp/category.html'
    queryset = []


class CartView(ListView):
    template_name = 'mainapp/cart.html'
    queryset = []
