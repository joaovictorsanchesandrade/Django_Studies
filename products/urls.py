from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('<slug:slug>', views.detail_view, name='detail'),
    path('', views.list_view, name='list')
]