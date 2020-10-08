from django.db import models

class Site(models.Model):
        id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
        name= models.CharField(max_length=255, blank=True, null=True)
        logo= models.ImageField(null=True)
        url= models.CharField(max_length=255, blank=True, null=True)
        info= models.TextField()

        class Meta:
            managed = 'True'
            db_table = 'Site'
