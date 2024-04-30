from django.db import models

"""
We will have customer table to store customer records.
Along with that we will have to store products data
We will create a purchases table that will store record of which
customer bought which product
"""

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    inventory_left = models.BigIntegerField()

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return f"{self.product_name}" 

class Customer(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=500)

    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 
    
class Purchase(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'Purchase'

# tables created issue of error it gives on their name
