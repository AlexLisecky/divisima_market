# Generated by Django 3.2 on 2021-12-27 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='product_main_image/', verbose_name='Изображение'),
        ),
    ]