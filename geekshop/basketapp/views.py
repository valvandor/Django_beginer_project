from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    content = {
        'title': title,
        'basket_items': basket_items,
    }
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, product_id):
    # FIXME: add a confirmation mechanism with a form and sending data using the POST method
    basket_record = get_object_or_404(Basket, pk=product_id)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))