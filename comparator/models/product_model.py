from django.db import models

class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name= models.CharField(max_length=255, blank=True,null=True)
    lowcategory= models.ForeignKey('LowCategory', models.DO_NOTHING, db_column='lowcategory', blank=True, null=True)
    info=models.TextField()

    class Meta:
            managed = 'True'
            db_table = 'Product'
