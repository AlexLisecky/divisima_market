import logging
import random

from django.http import HttpResponseNotFound
from django.views.generic import ListView, DetailView

from .models import Product, Category, ProductImage, Color

logger = logging.getLogger('main')


class IndexView(ListView):
    """ Главная страница """
    template_name = 'mainapp/index.html'
    model = Product
    queryset = Product.objects.all()[:8]
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = Color.objects.all().order_by('title')
        lst = []
        # context['latest_products'] = Product.objects.filter(created_at__gte=datetime.date.today())[:5]
        context['latest_products'] = Product.objects.all().order_by('-created_at')[:4]
        return context


class ProductView(DetailView):
    """ Страница продукта """
    model = Product
    template_name = 'mainapp/product.html'
    context_object_name = 'product'
    extra_context = {'category_page': 'Product'}


class ContactView(ListView):
    """ Страница контакты"""
    model = Product
    template_name = 'mainapp/contact.html'
    queryset = Product.objects.all()[:4]
    context_object_name = 'products'
    extra_context = {'category_page': 'Contact'}


class CheckoutView(ListView):
    """ Страница проверки"""
    template_name = 'mainapp/checkout.html'
    queryset = []
    extra_context = {'category_page': 'Cart'}


class CategoryView(DetailView):
    """ Страница категорий """
    model = Category
    template_name = 'mainapp/category.html'
    context_object_name = 'category'
    slug_field = 'url'
    extra_context = {'category_page': 'Category'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CartView(ListView):
    """ Страница карт"""
    template_name = 'mainapp/cart.html'
    model = Product
    context_object_name = 'products'
    extra_context = {'category_page': 'Cart'}

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
    """ Страница 404 не найдено """
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
