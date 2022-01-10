from django.db import models
from django.urls import reverse


class Category(models.Model):
    """ Модель Категория """
    name = models.CharField(verbose_name='Название', max_length=100)
    url = models.SlugField(verbose_name='Слаг', max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """ Модель Продукт """
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=500)
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=7)
    is_available = models.BooleanField(verbose_name='В наличии')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата обновления', auto_now=True)
    category = models.ManyToManyField(Category, verbose_name='Категории', related_name='product_category')
    image = models.ImageField(verbose_name='Изображение', upload_to='product_main_image/', default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    """ Модель Изображение продукта """
    name = models.CharField(verbose_name='Название', max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение', upload_to='product_image/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображение товаров'
