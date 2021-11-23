from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY =(
        ('Indoor','Indoor'),
        ('Out door','Out door')
    )
    name = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    desciption = models.CharField(max_length=300,null=True)
    creation_date = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered')
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    def __str__(self):
        return self.product.name + " Of "+self.customer.name