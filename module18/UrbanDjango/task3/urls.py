from django.urls import path
from .views import platform_view, shop_view, cart_view

urlpatterns = [
    path('', platform_view, name='platform'),  # Главная страница
    path('games/', shop_view, name='shop'),    # Путь для магазина
    path('cart/', cart_view, name='cart'),     # Корзина
]
