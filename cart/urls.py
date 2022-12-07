from . import views
from django.urls import path

app_name='cart'
urlpatterns = [
    path('', views.cartpage, name = 'cart'),
    path('addvaluetocart/', views.addvaluetocart, name = 'addvaluetocart'),
    path('removevaluetocart/', views.removevaluetocart, name = 'removevaluetocart'),
]
