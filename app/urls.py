from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('deconnexion/',deconnexion,name='deconnexion'),
    path('product/<int:id>/',productDetail,name='productdetail'),
    path('add-product/',createProduct,name='createproduct'),
    path('add-mark/',createMark,name='createmark'),
    path('all_product/',products,name='products'),
    path('cart/',cart,name='cart'),
    path('account/',account,name='account'),
   


]
