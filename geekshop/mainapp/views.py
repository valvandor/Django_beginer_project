from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product


def get_basket(user):
    return [] if not user.is_authenticated else Basket.objects.filter(user=user)


def index(request):
    title = 'магазин'
    basket = get_basket(request.user)
    content = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context=content)


def get_hot_product():
    from random import sample
    products = Product.objects.all()  # FIXME: not good to get all products from db
    return sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products_main(request):
    title = 'продукты'
    categories = ProductCategory.objects.all()
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        'title': title,
        'categories': categories,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/products_main.html', content)


def products_category(request, category_name=None):
    categories = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if category_name is not None:
        # processing the pseudo category
        if category_name == 'all':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все', 'description': 'какое-то описание'}
            title = 'продукты | все'
        # processing a category from a database
        else:
            category = get_object_or_404(ProductCategory, en_name=category_name)
            products = Product.objects.filter(category__en_name=category_name).order_by('price')
            title = f'продукты | {category.name}'

        content = {
            'title': title,
            'categories': categories,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products_list.html', content)

    products = Product.objects.all()

    title = 'продукты'

    content = {
        'title': title,
        'categories': categories,
        'products': products,
        'basket': basket,
    }

    return render(request, 'mainapp/products_main.html', context=content)


def product_detail(request, product_id):
    categories = ProductCategory.objects.all()
    basket = get_basket(request.user)
    active_product = get_object_or_404(Product, pk=product_id)
    title = f'{active_product}'
    same_products = get_same_products(active_product)
    content = {
        'title': title,
        'categories': categories,
        'active_product': active_product,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/product_detail.html', content)


def contact(request):
    title = 'контакты'
    basket = get_basket(request.user)

    content = {
        'title': title,
        'basket': basket,
    }

    return render(request, 'mainapp/contact.html', context=content)
