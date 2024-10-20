from django.shortcuts import render

def class_view(request):
    return render(request, 'second_task/class_template.html')

def function_view(request):
    return render(request, 'second_task/function_template.html')
from django.shortcuts import render

# Create your views here.
