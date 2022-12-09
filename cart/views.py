from detailpage.models import ProductModel, PrimaryCategoryModel
from django.shortcuts import render
from detailpage.models import ProductModel


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


def cartpage(request):
    value = sum(get_total_products_quantiy(request))
    products_in_cart = get_products_in_cart(request)
    products_quantity_in_cart = get_total_products_quantiy(request)
    price = get_price(request)
    mylists = zip(products_in_cart, products_quantity_in_cart,price)
    total_cost=sum(get_price(request))
    category = PrimaryCategoryModel.objects.all()
    context = {
        'mylist':mylists,
        'total_cost':total_cost,
        'categories':category,
        'cart_item_count':value,
    }
    if value == 0:
        return render(request, 'cart/cart_no_products.html', context)
    else:
        return render(request, 'cart/cart.html', context)

def addvaluetocart(request):

    id = request.POST['product_id']
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


def removevaluetocart(request):
    id = request.POST['product_id']
    if request.session.get(f'product_{id}_quantity', False):

        if int(request.session[f'product_{id}_quantity']) > 1 :
            request.session[f'product_{id}'] = id
            request.session[f'product_{id}_quantity'] -= 1
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
            try:
                del request.session[f'product_{id}']
                del request.session[f'product_{id}_quantity']
                print(request.session.items())
                print('secondlast')
                products_in_cart = get_products_in_cart(request)
                products_quantity_in_cart = get_total_products_quantiy(request)
                price = get_price(request)
                mylists = zip(products_in_cart, products_quantity_in_cart,price)
                total_cost=sum(get_price(request))
                context = {
                    'mylist':mylists,
                    'total_cost':total_cost,
                }
                return render(request, r'snippets/no_products.html', context)
            except:
                print(request.session.items())
                print('last')
                products_in_cart = get_products_in_cart(request)
                products_quantity_in_cart = get_total_products_quantiy(request)
                price = get_price(request)
                mylists = zip(products_in_cart, products_quantity_in_cart,price)
                total_cost=sum(get_price(request))
                context = {
                    'mylist':mylists,
                    'total_cost':total_cost,
                }
                return render(request, r'snippets/no_products.html', context)
    else:
        print(request.session.items())
        print('last')
        products_in_cart = get_products_in_cart(request)
        products_quantity_in_cart = get_total_products_quantiy(request)
        price = get_price(request)
        mylists = zip(products_in_cart, products_quantity_in_cart,price)
        total_cost=sum(get_price(request))
        context = {
            'mylist':mylists,
            'total_cost':total_cost,
        }
        return render(request, r'snippets/no_products.html', context)