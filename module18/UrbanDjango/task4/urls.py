from django.urls import path
from .views import platform_view, shop_view, cart_view

urlpatterns = [
    path('', platform_view, name='platform'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
]
