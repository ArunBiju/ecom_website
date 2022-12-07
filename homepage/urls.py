from . import views
from django.urls import path


app_name = 'homepage'
urlpatterns = [
    path('', views.homepage, name ='homepage'),
    path('sort/', views.sortby, name ='sort'),
    path('buynow/<slug:slug>/', views.buynow, name ='buynow'),
    path('addtocart/', views.addtocart, name ='addvaluetocart'),
]
