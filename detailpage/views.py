from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView
from detailpage.models import ProductModel


def detailpage(request, slug):
    product = ProductModel.objects.get(slug=slug)
    discount = int((product.selling_price/product.mrp)*100)
    value = sum(get_total_products_quantiy(request))
    return render(request, 'detailpage\detailpage.html', {'product':product, 'discount':discount, 'cart_item_count':value })

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

def addvaluetocart(request):
    id = request.POST['product_id']
    if request.session.get(f'product_{id}_quantity', False): 
        request.session[f'product_{id}'] = id
        request.session[f'product_{id}_quantity'] += 1
        print(request.session.items())
        return HttpResponse(sum(get_total_products_quantiy(request)))  
    else:
        request.session[f'product_{id}'] = id
        request.session[f'product_{id}_quantity'] = 1
        print(request.session.items())
        return HttpResponse(sum(get_total_products_quantiy(request)))

def removevaluetocart(request):
    id = request.POST['product_id']
    if request.session.get(f'product_{id}_quantity', False):

        if int(request.session[f'product_{id}_quantity']) > 1 :
            request.session[f'product_{id}'] = id
            request.session[f'product_{id}_quantity'] -= 1
            print(request.session.items())
            return HttpResponse(sum(get_total_products_quantiy(request)))
        else:
            try:
                del request.session[f'product_{id}']
                del request.session[f'product_{id}_quantity']
                print(request.session.items())
                print('secondlast')
                return HttpResponse(sum(get_total_products_quantiy(request)))
            except:
                print(request.session.items())
                print('last')
                return HttpResponse(sum(get_total_products_quantiy(request)))
    else:
        print(request.session.items())
        print('last')
        return HttpResponse(sum(get_total_products_quantiy(request)))


        # request.session.flush()
        # print(request.session.items())
        # return HttpResponse('0')

            
        

    





   
   
