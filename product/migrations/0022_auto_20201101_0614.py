# Generated by Django 3.1.1 on 2020-11-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20201101_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
