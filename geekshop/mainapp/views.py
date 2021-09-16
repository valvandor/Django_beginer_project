from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product


def index(request):
    title = 'магазин'
    content = {
        'title': title,
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, slug=None):
    title = f'продукты'
    categories = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if slug is not None:
        if slug == 'all':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все', 'description': 'какое-то описание'}
        else:
            category = get_object_or_404(ProductCategory, en_name=slug)
            products = Product.objects.filter(category__en_name=slug).order_by('price')

        content = {
            'title': title,
            'categories': categories,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products_list.html', content)

    products = Product.objects.all()

    content = {
        'title': title,
        'categories': categories,
        'products': products,
    }

    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    title = 'контакты'
    content = {
        'title': title,
    }

    return render(request, 'mainapp/contact.html', context=content)
