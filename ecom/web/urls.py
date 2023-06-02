from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact1,name="contact"),
    path('detail',views.detail,name="detail"),
    path('price',views.price,name="price"),
    path('product',views.product,name="product"),
    path('service',views.service,name="service"),
    path('team',views.team,name="team"),
    path('testimonial',views.testimonial,name="testimonial"),
    path('Login',views.Login1,name="login"),
    path('Sign Up',views.register,name="register"),
    path('logout',views.logout1,name="logout"),


    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart'),
    path('checkout',views.checkout,name="checkout"),
    path('placeorder',views.placeorder,name="placeorder"),
    path('confirm',views.confirm,name="confirm"),
    
  
]