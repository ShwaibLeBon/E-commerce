from django.urls import path
from .views import *

urlpatterns = [
    path('user-profil/',profile,name='profil'),
    path('user-home/',home,name='home'),
    path('user-deconnexion/',deconnexion,name='deconnexion'),
]
