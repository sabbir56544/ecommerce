# Generated by Django 3.1.1 on 2020-10-10 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='carts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.cart'),
        ),
    ]