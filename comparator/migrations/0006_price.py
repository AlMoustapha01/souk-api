# Generated by Django 3.0.5 on 2020-08-01 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comparator', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('stock_status', models.BooleanField(null=True)),
                ('url', models.URLField(null=True)),
                ('date_add', models.DateTimeField(auto_now=True, null=True)),
                ('product', models.ForeignKey(blank=True, db_column='product', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comparator.Product')),
                ('site', models.ForeignKey(blank=True, db_column='site', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comparator.Site')),
            ],
        ),
    ]
