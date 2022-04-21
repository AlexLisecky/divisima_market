from django.contrib import admin
from .models import Product, ProductImage, Category, Color
from django import forms
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)


class SliderFormAdmin(forms.ModelForm):
    class Meta:
        fields = '__all__'

        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }

@admin.register(Color)
class SliderAdmin(admin.ModelAdmin):
    form = SliderFormAdmin