from django.shortcuts import render

links_menu = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'product', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


def main(request):
    content = {
        'title': 'магазин',
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/index.html', context=content)


def products(request):
    content = {
        'title': 'продукты',
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    content = {
        'title': 'контакты',
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/contact.html', context=content)
