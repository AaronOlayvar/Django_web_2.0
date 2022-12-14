from django.shortcuts import render
from store.models import Product

def category_detail(request, slug):
    return render(request, 'store/category_detail.html')
# Create your views here.
def frontpage(request):
    products = Product.objects.filter(status= Product.ACTIVE)[0:10]

    return render(request,'core/frontpage.html', { 'products': products})

def about(request):
    return render( request, 'core/about.html')