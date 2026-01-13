from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpRequest
from .models import Product

# Create your views here.
def detail_view(request: HttpRequest, slug: str):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'products/detail.html', {'product': product})

def list_view(request: HttpRequest):
    products = Product.objects.filter(available=True)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/list.html', {
        'page_obj':page_obj
    })