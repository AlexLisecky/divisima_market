# Generated by Django 3.2 on 2022-04-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20220421_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
                ('img', models.ImageField(upload_to='frontend/images')),
            ],
        ),
    ]
