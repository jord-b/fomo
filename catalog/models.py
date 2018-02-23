from django.db import models
from polymorphic.models import PolymorphicModel

class Category(models.Model):
    '''Category for products'''
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(PolymorphicModel):
    '''a bulk, individual, or rental product'''
    TYPE_CHOICES = (
        ( 'BulkProduct', 'Bulk Product' ),
        ( 'IndividualProduct', 'Individual Product' ),
        ( 'RentalProduct', 'Rental Product' ),
    )

    STATUS_CHOICES = (
        ( 'A', 'Active' ),
        ( 'I', 'Inactive' ),
    )
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS_CHOICES,default='A')
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)

class BulkProduct(Product):
    '''a bulk product'''
    TITLE = 'Bulk'
    quantity = models.IntegerField()
    reorder_Trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()

class IndividualProduct(Product):
    '''an individual product'''
    TITLE = 'Individual'
    pid = models.TextField()

class RentalProduct(Product):
    '''products only available for rent(tracked individually)'''
    TITLE = 'Rental'
    pid = models.TextField()
    max_rental_days = models.IntegerField(default=0)
    retire_date = models.DateField(null=True, blank=True)


# Create your models here.
