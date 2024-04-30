from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('products', views.product_records, name='products'),
    path('purchases', views.purchase_records, name='purchases'),
    path('update_customer/<int:cid>', views.update_customer, name='update_customer'),    
    path('delete_customer/<int:cid>', views.delete_customer, name='delete_customer'),    
    path('add_customer', views.add_customer, name='add_customer'),    
    path('add_products', views.add_product, name='add_product'),    
    path('update_product/<int:pid>', views.update_product, name='update_product'),    
    path('delete_product/<int:pid>', views.delete_product, name='delete_product'),    
    path('add_purchases', views.add_purchases, name='add_purchases'),    
    path('delete_purchase/<int:prid>', views.delete_purchase, name='delete_purchase'),    
    # path('set_cookie', views.set_cookie, name='set_cookie'),    

]
