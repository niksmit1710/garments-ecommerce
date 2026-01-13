from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand, Size

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_available=True)

    brand = request.GET.get('brand')
    size = request.GET.get('size')
    price = request.GET.get('price')

    if brand:
        products = products.filter(brand__slug=brand)

    if size:
        products = products.filter(sizes__id=size)

    if price:
        products = products.filter(price__lte=price)

    context = {
        'category': category,
        'products': products,
        'brands': Brand.objects.all(),
        'sizes': Size.objects.all(),
    }
    return render(request, 'products/product_list.html', context)
def product_detail(request, id):
    product = get_object_or_404(Product, id=id, is_available=True)
    return render(request, 'products/product_detail.html', {
        'product': product
    })
