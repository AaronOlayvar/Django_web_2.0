from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from .models import Product, Category

from .forms import OrderForm

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status= Product.ACTIVE)
    return render(request, 'store/category_detail.html', {'category': category, 'products': products})


# Create your views here.
def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)

    return render(request, 'store/product_detail.html', {'product': product})


def search(request):
    query = request.GET.get('query','')
    products = Product.objects.filter(status= Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'store/search.html', {'query':query, 'products': products, })

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect ('cart_view')

def cart_view(request):
    cart = Cart(request)

    return render(request, 'store/cart_view.html', {'cart': cart})

@login_required
def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            return redirect('myaccount')
    else:
        form = OrderForm()

    return render(request, 'store/checkout.html', {'cart': cart, 'form': form})

def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity= -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)
        
        return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')
