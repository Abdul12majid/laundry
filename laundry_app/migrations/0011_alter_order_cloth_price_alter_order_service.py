# Generated by Django 4.0.3 on 2024-02-10 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0010_order_cloth_price_order_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cloth_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
