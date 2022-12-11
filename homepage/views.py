from django.http import HttpResponse
from django.shortcuts import redirect, render
from detailpage.models import ProductModel, PrimaryCategoryModel, SecondaryCategoryModel
from django.db.models import Q
from detailpage.views import addvaluetocart
from .models import HomepageImage
from django.core.paginator import Paginator, EmptyPage


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


def sort(request):
    value = sum(get_total_products_quantiy(request))
    hpimage = HomepageImage.objects.get(pk=1)
    hpbanner = HomepageImage.objects.get(pk=2)
    category = PrimaryCategoryModel.objects.all()
    search_term = (request.POST.get('search',None))
    print(search_term)
    products = ProductModel.objects.filter(Q(name__contains=search_term)|Q(details__contains=search_term))
    context = {
        'products':products,
        'categories':category,   
        'cart_item_count':value,
        'hpimage':hpimage,
        'hpbanner':hpbanner,
        'categories':category,
    }
    if len(products) == 0:
        return render(request, 'homepage/snippets/homepage_search_no_result.html', context)
    else:
        return render(request, 'homepage/snippets/homepage_search.html', context)
    

def category(request):

    search_term = (request.POST.get('category'))
    products = PrimaryCategoryModel.objects.all()
    context = {
        'products':category,
    }
    return render(request, 'homepage/snippets/cards.html', context)

def primary(request, id):

    primary_category = PrimaryCategoryModel.objects.get(id=id)
    products_in_category = primary_category.productmodel_set.all()
    value = sum(get_total_products_quantiy(request))
    category = PrimaryCategoryModel.objects.all()
    hpimage = HomepageImage.objects.get(pk=1)
    categoryimage = PrimaryCategoryModel.objects.get(pk=1)
    hpbanner = HomepageImage.objects.get(pk=2)
    print(products_in_category)
    context = {
        'products':products_in_category,
        'cart_item_count':value,
        'hpimage':hpimage,
        'hpbanner':hpbanner,
        'categories':category,
        'current_category':primary_category,
    }
    
    if len(products_in_category) == 0:
        return render(request, 'homepage/snippets/homepage_search_no_result.html', context)
    else:
        return render(request, 'homepage/snippets/homepage_search.html', context)

def secondary(request, id):

    category = SecondaryCategoryModel.objects.get(id=id)
    products_in_category = category.productmodel_set.all()
    value = sum(get_total_products_quantiy(request))
    category = PrimaryCategoryModel.objects.all()
    secondary = SecondaryCategoryModel.objects.get(id=id)
    hpimage = HomepageImage.objects.get(pk=1)
    hpbanner = HomepageImage.objects.get(pk=2)
    categoryimage = PrimaryCategoryModel.objects.get(pk=1)
    context = {
        'products':products_in_category,
        'cart_item_count':value,
        'secondary':secondary,
        'hpimage':hpimage,
        'hpbanner':hpbanner,
        'categories':category,
        'category_image':categoryimage,
    }
    
    if len(products_in_category) == 0:
        return render(request, 'homepage/snippets/no_result_secondary.html', context)
    else:
        return render(request, 'homepage/snippets/search_secondary.html', context)

def buynow(request,slug):
    addvaluetocarthp(request,slug)
    return redirect('cart:cart')

def addtocart(request):
    addvaluetocart(request)
    return HttpResponse(sum(get_total_products_quantiy(request))) 

def listing(request, page):
    value = sum(get_total_products_quantiy(request))
    products = ProductModel.objects.all()
    category = PrimaryCategoryModel.objects.all()
    hpimage = HomepageImage.objects.get(pk=1)
    hpbanner = HomepageImage.objects.get(pk=2)
    paginator = Paginator(products, per_page=6)
    try:
        page_object = paginator.page(page)
    except EmptyPage:
        page_object = paginator.page(1)
    print(paginator.get_page(1))
    context = {
        'products':products,
        'cart_item_count':value,
        'hpimage':hpimage,
        'hpbanner':hpbanner,
        'categories':category,
        "page_obj": page_object
    }
    return render(request, 'homepage/index_pagenation.html', context)

def homepage(request):   
    value = sum(get_total_products_quantiy(request))
    products = ProductModel.objects.all()
    category = PrimaryCategoryModel.objects.all()
    hpimage = HomepageImage.objects.get(pk=1)
    hpbanner = HomepageImage.objects.get(pk=2)
    paginator = Paginator(products, per_page=6)
    page_object = paginator.page(1)
    print(paginator.get_page(1))
    context = {
        'products':products,
        'cart_item_count':value,
        'hpimage':hpimage,
        'hpbanner':hpbanner,
        'categories':category,
        "page_obj": page_object
    }
    return render(request, 'homepage/index_pagenation.html', context)