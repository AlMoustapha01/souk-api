from django.db import models

class Price(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    value= models.CharField(max_length=255, blank=True,null=True)
    product= models.ForeignKey('Product', models.DO_NOTHING, db_column='product', blank=True, null=True)
    site= models.ForeignKey('Site', models.DO_NOTHING, db_column='site', blank=True, null=True)
    stock_status=models.BooleanField(null=True)
    url=models.URLField(null=True)
    date_add=models.DateTimeField(auto_now=True,null=True)

    class Meta:
            managed = 'True'
            db_table = 'Price'
