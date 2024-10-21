from django.shortcuts import render

def platform_view(request):  # Обновлённое название функции
    return render(request, 'third_task/platform.html')  # Обновлённый шаблон

def shop_view(request):
    products = {
        'Игра 1': '$59.99',
        'Игра 2': '$49.99',
        'Игра 3': '$39.99',
    }
    return render(request, 'third_task/shop.html', {'products': products})

def cart_view(request):
    return render(request, 'third_task/cart.html')
