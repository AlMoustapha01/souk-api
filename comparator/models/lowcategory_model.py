from django.db import models

class LowCategory(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name= models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='category', blank=True, null=True)

    class Meta:
            managed = 'True'
            db_table = 'LowCategory'



