from django.shortcuts import render


def basket(request):
    title = 'корзина'
    content = {'title': title}
    return render(request, 'basketapp/basket.html', content)
