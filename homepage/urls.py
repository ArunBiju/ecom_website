from . import views
from django.urls import path


app_name = 'homepage'
urlpatterns = [
    path( "home/<int:page>",views.listing,name="terms-by-page"),
    path('', views.homepage, name ='homepage'),
    path('sort/', views.sort, name ='sort'),
    path('buynow/<slug:slug>/', views.buynow, name ='buynow'),
    path('addtocart/', views.addtocart, name ='addvaluetocart'),
    path('category/', views.category, name ='category'),
    path('primary/<int:id>/', views.primary, name ='primary'),
    path('secondary/<int:id>/', views.secondary, name ='secondary'),
    
]
