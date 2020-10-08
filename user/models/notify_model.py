from django.db import models

class Notify(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title= models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('Users',on_delete=models.CASCADE,db_column='users', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
            managed = 'True'
            db_table = 'Notify'


