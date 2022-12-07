from django.http import HttpResponse
from django.shortcuts import redirect, render
from detailpage.models import ProductModel
from django.db.models import Q
from detailpage.views import addvaluetocart


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

def get_price(request):

    price = []

    products_in_cart = get_products_in_cart(request)
    products_quantity_in_cart = get_total_products_quantiy(request)
    mylists = zip(products_in_cart, products_quantity_in_cart)
    for product,quantity in mylists:
        print(product.selling_price*quantity)
        price.append(product.selling_price*quantity)
    return price

def addvaluetocarthp(request,slug):

    id = slug
    if request.session.get(f'product_{id}_quantity', False): 
        request.session[f'product_{id}'] = id
        request.session[f'product_{id}_quantity'] += 1
        print(request.session.items())
        products_in_cart = get_products_in_cart(request)
        products_quantity_in_cart = get_total_products_quantiy(request)
        price = get_price(request)
        mylists = zip(products_in_cart, products_quantity_in_cart,price)
        total_cost=sum(get_price(request))
        context = {
            'mylist':mylists,
            'total_cost':total_cost,
        }
        return render(request, r'snippets/cards.html', context)
    else:
        request.session[f'product_{id}'] = id
        request.session[f'product_{id}_quantity'] = 1
        products_in_cart = get_products_in_cart(request)
        products_quantity_in_cart = get_total_products_quantiy(request)
        price = get_price(request)
        mylists = zip(products_in_cart, products_quantity_in_cart,price)
        total_cost=sum(get_price(request))
        context = {
            'mylist':mylists,
            'total_cost':total_cost,
        }
        return render(request, r'snippets/cards.html', context)

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

def buynow(request,slug):
    addvaluetocarthp(request,slug)
    return redirect('cart:cart')

def addtocart(request):
    addvaluetocart(request)
    return HttpResponse(sum(get_total_products_quantiy(request))) 

