from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(
        category=category,
        is_available=True
    )

    subcategories = category.subcategories.all()

    context = {
        'category': category,
        'products': products,
        'subcategories': subcategories,
    }
    return render(request, 'products/product_list.html', context)
