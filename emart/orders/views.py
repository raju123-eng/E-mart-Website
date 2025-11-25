from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_list(request):
    if request.user.user_type == 'buyer':
        orders = Order.objects.filter(buyer=request.user)
    elif request.user.user_type == 'seller':
        # seller sees orders with items belonging to them
        orders = Order.objects.filter(items__seller__user=request.user).distinct()
    else:
        orders = Order.objects.all()
    return render(request, 'orders/list.html', {'orders':orders})

@login_required
def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    return render(request, 'orders/detail.html', {'order':order})
