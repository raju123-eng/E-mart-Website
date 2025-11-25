from django.urls import path
from . import views

app_name = 'payments'
urlpatterns = [
    path('pay/<int:order_id>/', views.pay_order, name='pay_order'),
    path('callback/razorpay/', views.razorpay_callback, name='razorpay_callback'),
]
