from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Product

# Create your views here.
def product_view(request: HttpRequest, slug: str):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'products/detail.html', {'product': product})