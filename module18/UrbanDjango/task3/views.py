from django.shortcuts import render

def platform_view(request):
    pagename = "Платформа"
    content = "<p>Добро пожаловать на нашу игровую платформу!</p>"
    return render(request, 'third_task/platform.html', {'pagename': pagename, 'content': content})

def shop_view(request):
    pagename = "Магазин"
    products = {
        'Игра 1': '$59.99',
        'Игра 2': '$49.99',
        'Игра 3': '$39.99',
    }
    content = "<p>Выберите свои любимые игры из нашего магазина.</p>"
    return render(request, 'third_task/shop.html', {'pagename': pagename, 'products': products, 'content': content})

def cart_view(request):
    pagename = "Корзина"
    content = "<p>Ваша корзина пуста. Пожалуйста, добавьте что-нибудь в неё.</p>"
    return render(request, 'third_task/cart.html', {'pagename': pagename, 'content': content})
