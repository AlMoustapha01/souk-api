from django.db import models
from comparator.models.price_model import *

class FollowPrice(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    price = models.ForeignKey(Price,on_delete=models.CASCADE,db_column='price', blank=True, null=True)
    user = models.ForeignKey('Users',on_delete=models.CASCADE,db_column='users', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
            managed = 'True'
            db_table = 'FollowPrice'


