from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from cart.models import Cart, CartItem, Product

@login_required
def detail_view(request: HttpRequest):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/detail.html', {'cart': cart})

@login_required
def add_to_cart_view(request: HttpRequest, slug: str):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:detail')

@login_required
def remove_to_cart_view(request: HttpRequest, slug: str):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item = get_object_or_404(CartItem, product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:detail')