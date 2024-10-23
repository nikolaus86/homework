from django.shortcuts import render

def platform_view(request):
    return render(request, 'fourth_task/platform.html')

def shop_view(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'The Witcher 3']
    return render(request, 'fourth_task/shop.html', {'games': games})

def cart_view(request):
    return render(request, 'fourth_task/cart.html')
