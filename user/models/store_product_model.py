from django.db import models
from comparator.models.product_model import *

class StoreProduct(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,db_column='product', blank=True, null=True)
    user = models.ForeignKey('Users',on_delete=models.CASCADE,db_column='users', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
            managed = 'True'
            db_table = 'StoreProduct'


