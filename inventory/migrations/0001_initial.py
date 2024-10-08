# Generated by Django 5.0.6 on 2024-07-30 17:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(blank=True, db_index=True, null=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('product_id', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('unit_price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('qty_available', models.PositiveIntegerField(default=0, null=True)),
                ('qty_sold', models.PositiveIntegerField(default=0, null=True)),
                ('qty_purchased', models.PositiveIntegerField(default=0, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
