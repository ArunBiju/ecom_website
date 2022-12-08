from . import views
from django.urls import path


app_name = 'homepage'
urlpatterns = [
    path('', views.homepage, name ='homepage'),
    path('sort/', views.sortby, name ='sort'),
    path('buynow/<slug:slug>/', views.buynow, name ='buynow'),
    path('addtocart/', views.addtocart, name ='addvaluetocart'),
    path('category/', views.category, name ='category'),
    path('primary/<int:id>/', views.primary, name ='primary'),
    path('secondary/<int:id>/', views.secondary, name ='secondary')
]
