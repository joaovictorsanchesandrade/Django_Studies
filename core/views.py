from django.shortcuts import render
from products.models import Product

def index_view(request):
    products = Product.objects.filter(available=True)[:8]
    return render(request, 'core/index.html', {'products': products})