from django.contrib import admin
from django.urls import path, include

from .views import IndexView, CartView, CategoryView, CheckoutView, ContactView, ProductView

app_name = 'mainapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cart/', CartView.as_view(), name='cart'),
    path('category/', CategoryView.as_view(), name='category'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/', ProductView.as_view(), name='product')
]
