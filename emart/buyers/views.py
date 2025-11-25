from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from orders.models import Order, OrderItem
from decimal import Decimal
from django.contrib.auth.decorators import login_required

def home(request):
    products = Product.objects.all().order_by('-created_at')[:20]
    return render(request,'buyers/home.html', {'products':products})

def _get_cart(request):
    return request.session.get('cart', {})

def add_to_cart(request, product_id):
    cart = _get_cart(request)
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = _get_cart(request)
    items = []
    total = Decimal('0.00')
    for pid, qty in cart.items():
        p = get_object_or_404(Product, pk=int(pid))
        items.append({'product':p,'quantity':qty,'subtotal': p.price * qty})
        total += p.price * qty
    return render(request, 'buyers/cart.html', {'items': items, 'total': total})

@login_required
def checkout(request):
    cart = _get_cart(request)
    if not cart:
        return redirect('home')
    # create Order
    order = Order.objects.create(buyer=request.user, total=0, shipping_address=request.user.address or '')
    total = 0
    for pid, qty in cart.items():
        p = get_object_or_404(Product, pk=int(pid))
        OrderItem.objects.create(order=order, product=p, price=p.price, quantity=qty, seller=p.seller)
        total += p.price * qty
        # reduce stock
        p.stock = max(0, p.stock - qty)
        p.save()
    order.total = total
    order.save()
    # clear cart
    request.session['cart'] = {}
    # redirect to payment page for order
    return redirect('payments:pay_order', order_id=order.id)
