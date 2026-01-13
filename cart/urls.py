from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('add_to_cart/<slug:slug>', views.add_to_cart_view, name='add'),
    path('remove_to_cart/<slug:slug>', views.remove_to_cart_view, name='remove'),
    path('detail', views.detail_view, name='detail')
]  