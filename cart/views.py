from django.shortcuts import redirect, render
from .cart import Cart
from django.views.decorators.http import require_POST


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('cart:cart_detail')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@require_POST
def update_cart(request, product_id):
    qty = int(request.POST.get('qty'))
    cart = Cart(request)
    cart.update(product_id, qty)
    return redirect('cart:cart_detail')
