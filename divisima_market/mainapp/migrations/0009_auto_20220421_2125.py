# Generated by Django 3.2 on 2022-04-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20220421_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='from_pxl',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='color',
            name='to_pxl',
            field=models.SmallIntegerField(default=0),
        ),
    ]
