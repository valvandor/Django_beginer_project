from django.shortcuts import render
from .models import ProductCategory, Product

links_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'product', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


def index(request):
    title = 'магазин'
    content = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    categories = ProductCategory.objects.all()
    title = 'продукты'
    products = Product.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'categories': categories,
        'products': products,
    }
    return render(request, 'mainapp/products.html', context=content)


def products_category(request, slug):
    categories = ProductCategory.objects.all()
    active_category = ProductCategory.objects.get(en_name=slug)
    title = f'продукты | {active_category.name}'
    products = Product.objects.filter(category=active_category.id)

    content = {
        'title': title,
        'links_menu': links_menu,
        'categories': categories,
        'products': products,
    }

    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    title = 'контакты'
    content = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/contact.html', context=content)
