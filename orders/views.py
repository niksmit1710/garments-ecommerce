from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Order, OrderItem


@login_required(login_url='login')
def checkout(request):
    cart = Cart(request)

    if not cart.cart:
        return redirect('cart:cart_detail')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone')

        # 1️⃣ Create Order
        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            address=address,
            city=city,
            phone=phone,
            total_amount=cart.total_price()
        )

        # 2️⃣ Create Order Items
        for item in cart.items():
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['product'].price,
                quantity=item['qty']
            )

        # 3️⃣ Clear Cart
        request.session['cart'] = {}
        request.session.modified = True

        return render(request, 'orders/order_success.html', {
            'order': order
        })

    return render(request, 'orders/checkout.html', {
        'cart': cart
    })


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/my_orders.html', {
        'orders': orders
    })
