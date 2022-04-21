from django.contrib import admin
from .models import Product, ProductImage, Category, Color, ImgCategory, FooterImg
from django import forms
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)


class ColorFormAdmin(forms.ModelForm):
    class Meta:
        fields = '__all__'

        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }

admin.site.register(ImgCategory)

@admin.register(Color)
class SliderAdmin(admin.ModelAdmin):
    form = ColorFormAdmin


@admin.register(FooterImg)
class FooterAdmin(admin.ModelAdmin):
    form = ColorFormAdmin


def get_footer_color(request):
    footer = FooterImg.objects.all().first()
    return {'footer_color':footer}