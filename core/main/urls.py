from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('shop/',views.shop,name='shop'),
    path('cart/',views.cart,name='cart'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:cart_item_id>/', views.cart_remove, name='cart_remove'),
    path('shop_single/<int:product_id>/', views.shop_single, name='shop_single'),  
    path('contact/',views.contact,name='contact'),
    path('thankyou/',views.thankyou,name='thankyou'),

]

