# Generated by Django 3.0.5 on 2020-08-01 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comparator', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': 'True'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
    ]
