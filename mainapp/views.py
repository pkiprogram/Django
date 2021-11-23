from django.shortcuts import render

import json
import os

MODULE_DIR =os.path.dirname(__file__)
# Create your views here.

def index(request):
    context = {
        'title': 'Geekshop', }
    return render(request, 'mainapp/index.html', context)


def products(request):
        context = {
        'title': 'Geekshop | Каталог',
    }
        
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    
    return render(request, 'mainapp/products.html', context)
