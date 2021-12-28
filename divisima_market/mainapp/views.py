import datetime
import random
from django.views.generic import ListView, DetailView

from .models import Product, Category


class IndexView(ListView):
    """ Главная страница """
    template_name = 'mainapp/index.html'
    model = Product
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.filter(created_at__lte=datetime.date.today())[:5]
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'mainapp/product.html'
    context_object_name = 'product'


class ContactView(ListView):
    template_name = 'mainapp/contact.html'
    queryset = []


class CheckoutView(ListView):
    template_name = 'mainapp/checkout.html'
    queryset = []


class CategoryView(ListView):
    template_name = 'mainapp/category.html'
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context



class CartView(ListView):
    template_name = 'mainapp/cart.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        my_ids = Product.objects.values_list('id', flat=True)
        my_ids = list(my_ids)
        n = 4
        rand_ids = random.sample(my_ids, n)
        random_records = Product.objects.filter(id__in=rand_ids)
        context['random_products'] = random_records
        return context
