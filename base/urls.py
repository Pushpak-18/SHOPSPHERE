from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('cart/',cart,name='cart'),
    path('support/', support, name='support'),
    path('about/', about, name='about'),
    path('addtocart/<int:id>',addtocart,name='addtocart'),
    path('remove/<int:id>',remove,name='remove'),
    path('increment/<int:id>',increment,name='increment'),
    path('decrement/<int:id>',decrement,name='decrement')
]