# Generated by Django 3.1.1 on 2020-10-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20201026_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tranx_id',
            field=models.CharField(default='TrxID : ', max_length=50, unique=True),
        ),
    ]
