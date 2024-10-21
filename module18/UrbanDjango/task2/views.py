from django.shortcuts import render

def class_template_view(request):
    return render(request, 'second_task/template_class.html')

def function_template_view(request):
    return render(request, 'second_task/template_function.html')
