from django.shortcuts import render

links_menu = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'product', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

titles = {
    'main': 'магазин',
    'product': 'продукты',
    'contact': 'контакты',
}

content = {
    'links_menu': links_menu,
    'title': titles,
}


def main(request):
    return render(request, 'mainapp/index.html', context=content)


def products(request):
    return render(request, 'mainapp/products.html', context=content)


def contact(request):
    return render(request, 'mainapp/contact.html', context=content)
