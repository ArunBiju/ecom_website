from django.shortcuts import render
from django.views.generic import ListView
from detailpage.models import ProductModel
from django.db.models import Q

def get_products_in_cart(request):
    keys = request.session.keys()
    products =[]
    for key in keys:
        id =request.session.get(key)
        try:
            products_in_cart = ProductModel.objects.get(slug=id)
            products.append(products_in_cart)
        except:
            pass
    return products

def get_total_products_quantiy(request):
    id = get_products_in_cart(request)
    products_quantity =[]
    for product in id:
        try:
            quantiy_per_product = request.session[f'product_{product.slug}_quantity']
            products_quantity.append(quantiy_per_product)
        except:
            pass
    return products_quantity


def homepage(request):
    
    value = sum(get_total_products_quantiy(request))
    products = ProductModel.objects.all()
    context = {
        'products':products,
        'cart_item_count':value,
    }
    return render(request, 'homepage/index.html', context)

def sortby(request):

    search_term = (request.POST.get('search'))
    products = ProductModel.objects.filter(Q(name__contains=search_term)|Q(details__contains=search_term))
    context = {
        'products':products,
    }
    return render(request, 'homepage/snippets/cards.html', context)
