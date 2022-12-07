from . import views
from django.urls import path

app_name ='detailpage'
urlpatterns = [
    path('addvaluetocart/', views.addvaluetocart, name = 'addvaluetocart'),
    path('removevaluetocart/', views.removevaluetocart, name = 'removevaluetocart'),
    path('<slug:slug>/', views.detailpage, name = 'detailpage'),
]
