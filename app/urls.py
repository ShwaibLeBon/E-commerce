from django.urls import path
from .views import *

urlpatterns = [
    path('',profile,name='profile'),
    path('home/',home,name='home'),
    path('allproduct/',products,name='products'),
    path('addmark/',marque,name='marque'),
    path('product/<int:id>/',productDetail,name='productDetail'),
    path('addproduct/',createProduct,name='createProuct'),
    path('deconnexion/',deconnexion,name='deconnexion'),
]
