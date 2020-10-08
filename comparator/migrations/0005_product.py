# Generated by Django 3.0.5 on 2020-08-01 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comparator', '0004_lowcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('info', models.TextField()),
                ('lowcategory', models.ForeignKey(blank=True, db_column='lowcategory', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comparator.LowCategory')),
            ],
        ),
    ]
