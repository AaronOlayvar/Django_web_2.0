from django.shortcuts import render
from .models import Product


# Create your views here.
def product_detail(request):
    return render(request, 'store/product_detail.html')
