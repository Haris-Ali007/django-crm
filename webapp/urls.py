from django.urls import path, include
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
]
