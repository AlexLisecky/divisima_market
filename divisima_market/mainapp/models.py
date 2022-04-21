from django.db import models
from django.urls import reverse

class FooterImg(models.Model):
    color = models.CharField(max_length=10)
    img = models.ImageField(upload_to="frontend/images",blank=True)

    class Meta:
        verbose_name = 'Изменение футера'
        verbose_name_plural = 'Изменение футера'

    def __str__(self):
        return 'Футер'

class ImgCategory(models.Model):
    title = models.CharField(max_length=10)
    img = models.ImageField(upload_to="frontend/images/")

    class Meta:
        verbose_name = 'Картинки для основных категорий'
        verbose_name_plural = 'Картинки для основных категорий'

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Цвет для полоски под меню'
        verbose_name_plural = 'Цвет для полоски под меню'

    def __str__(self):
        return self.title

class Category(models.Model):
    """ Модель Категория """
    name = models.CharField(verbose_name='Название', max_length=100)
    url = models.SlugField(verbose_name='Слаг', max_length=160, db_index=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:category', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """ Модель Продукт """
    name = models.CharField(verbose_name='Название', max_length=100)
    description = models.CharField(verbose_name='Описание', max_length=500)
    price = models.DecimalField(verbose_name='Цена', decimal_places=2, max_digits=7)
    is_available = models.BooleanField(verbose_name='В наличии', default=False)
    is_new = models.BooleanField(verbose_name='Новинка', default=False)
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
