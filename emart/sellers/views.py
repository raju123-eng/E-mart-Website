from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SellerProfile
from products.models import Product
from products.forms import ProductForm
from django.http import HttpResponse     # add this at top if not added already

def product_edit(request, pk):
    return HttpResponse("Product edit page (temporary)")


@login_required
def dashboard(request):
    sp = getattr(request.user, 'sellerprofile', None)
    products = Product.objects.filter(seller=sp) if sp else []
    return render(request, 'sellers/dashboard.html', {'products':products})

@login_required
def product_add(request):
    sp = getattr(request.user, 'sellerprofile', None)
    if not sp:
        return redirect('sellers:dashboard')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.seller = sp
            p.save()
            return redirect('sellers:dashboard')
    else:
        form = ProductForm()
    return render(request, 'sellers/product_form.html', {'form':form})
