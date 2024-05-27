from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Category, Product, Section

from cart.forms import CartAddProductForm

# Create your views here.


@login_required
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    sections = Section.objects.all().prefetch_related('categories')
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/home.html', {'category': category, 'categories': categories, 'products': products, 'sections': sections})


@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})


@login_required
def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    cart_product_form = CartAddProductForm()

    return render(request, 'shop/product/category.html', {'products': products, 'category': category, 'cart_product_form': cart_product_form})
