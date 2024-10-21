from django.urls import path
from .views import class_template_view, function_template_view

urlpatterns = [
    path('class-view/', class_template_view, name='class_view'),
    path('function-view/', function_template_view, name='function_view'),
]
