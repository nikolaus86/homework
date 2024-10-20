from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def shop(request):
    items = {
        "Игровая приставка": "30000 рублей",
        "Игра A": "2000 рублей",
        "Игра B": "1500 рублей"
    }
    context = {"items": items}
    return render(request, 'third_task/shop.html', context)

def cart(request):
    return render(request, 'third_task/cart.html')
