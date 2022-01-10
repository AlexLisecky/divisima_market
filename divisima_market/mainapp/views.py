import datetime
import random

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Category


class IndexView(ListView):
    """ Главная страница """
    template_name = 'mainapp/index.html'
    model = Product
    queryset = Product.objects.all()[:8]
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_products'] = Product.objects.filter(created_at__gte=datetime.date.today())[:5]
        context['latest_products'] = Product.objects.all().order_by('-created_at')[:4]
        return context



class ProductView(DetailView):
    """ Страница продукта """
    model = Product
    template_name = 'mainapp/product.html'
    context_object_name = 'product'


class ContactView(ListView):
    model = Product
    template_name = 'mainapp/contact.html'
    queryset = Product.objects.all()[:4]
    context_object_name = 'products'


class CheckoutView(ListView):
    template_name = 'mainapp/checkout.html'
    queryset = []


class CategoryView(DetailView):
    model = Category
    template_name = 'mainapp/category.html'
    context_object_name = 'category'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CartView(ListView):
    template_name = 'mainapp/cart.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_ids = Product.objects.values_list('id', flat=True)
        my_ids = list(my_ids)
        n = 4
        rand_ids = random.sample(my_ids, n)
        random_records = Product.objects.filter(id__in=rand_ids)
        context['random_products'] = random_records
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
