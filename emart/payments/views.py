from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import razorpay
from orders.models import Order
from .models import Payment
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

client = None
if hasattr(settings, 'RAZORPAY_KEY') and hasattr(settings, 'RAZORPAY_SECRET'):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))

def pay_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if client is None:
        # fallback: mark as paid (testing) - DO NOT use in production
        order.status = 'paid'
        order.save()
        Payment.objects.create(order=order, provider='razorpay', amount=order.total, success=True)
        return redirect('orders:order_detail', pk=order.id)

    amount_paise = int(order.total * 100)
    razorpay_order = client.order.create(dict(amount=amount_paise, currency="INR", payment_capture=1))
    # save provider id if needed
    context = {'order':order, 'razorpay_order': razorpay_order, 'razorpay_key': settings.RAZORPAY_KEY, 'amount': order.total}
    return render(request,'payments/pay.html', context)

@csrf_exempt
def razorpay_callback(request):
    # implement signature verification and update payment record
    # For brevity, accept posted data and mark payment success (but verify in prod)
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method")
    data = request.POST
    # TODO: verify signature here using razorpay utilities
    order_id = data.get('order_id')  # your mapping depends on how you created the order
    # find order and mark paid
    # ...
    return render(request, 'payments/success.html')
