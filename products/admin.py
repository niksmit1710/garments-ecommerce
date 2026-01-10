from django.contrib import admin
from .models import Category, Product, Size, Brand

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Brand)