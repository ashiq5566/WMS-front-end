# Generated by Django 5.0.6 on 2024-10-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_rename_unit_price_product_price_at_time_of_purchase_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
