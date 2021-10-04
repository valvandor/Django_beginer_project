from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    content = {
        'title': title,
        'basket_items': basket_items,
    }
    return render(request, 'basketapp/basket.html', content)


@login_required
def basket_add(request, product_id):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product_detail', args=[product_id]))
    product = get_object_or_404(Product, pk=product_id)
    item_in_basket = Basket.objects.filter(user=request.user, product=product).first()

    if not item_in_basket:
        item_in_basket = Basket(user=request.user, product=product)

    item_in_basket.quantity += 1
    item_in_basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, product_id):
    # FIXME: add a confirmation mechanism with a form and sending data using the POST method
    basket_record = get_object_or_404(Basket, pk=product_id)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, product_id, quantity):
    if request.is_ajax():
        # FIXME: JS works, but with some bugs(errors with quantity, clicking not on the button also sends a request)
        quantity = int(quantity)
        editing_basket_item = Basket.objects.get(pk=int(product_id))
        if quantity > 0:
            editing_basket_item.quantity = quantity
            editing_basket_item.save()
        else:
            editing_basket_item.delete()
        basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
        content = {
            'basket_items': basket_items,
        }
        result = render_to_string('basketapp/includes/inc_basket_list.html', content)
        return JsonResponse({'result': result})
