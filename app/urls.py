from django.urls import path
from .views import *

urlpatterns = [
    path('',profile,name='profil'),
    path('home/',home,name='home'),
    path('product/<int:id>/',productDetails,name='productdetail'),
    path('add-product/',createProduct,name='createproduct'),
    path('add-mark/',productMark,name='productmark'),
    path('all-product/',products,name='products'),
    path('deconnexion/',deconnexion,name='deconnexion'),
]
