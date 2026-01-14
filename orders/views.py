from django.shortcuts import render, redirect
from cart.cart import Cart
from .models import Order

def checkout(request):
    cart = Cart(request)

    if not cart.cart:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone')

        order = Order.objects.create(
            full_name=full_name,
            address=address,
            city=city,
            phone=phone,
            total_amount=cart.total_price()
        )

        # clear cart after order
        request.session['cart'] = {}
        request.session.modified = True

        return render(request, 'orders/order_success.html', {
            'order': order
        })

    return render(request, 'orders/checkout.html', {
        'cart': cart
    })
