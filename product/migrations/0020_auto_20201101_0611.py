# Generated by Django 3.1.1 on 2020-11-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20201031_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]