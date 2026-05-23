from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'pname', 'pcategory']

admin.site.register(Product, ProductAdmin)