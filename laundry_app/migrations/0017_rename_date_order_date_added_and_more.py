# Generated by Django 4.0.3 on 2024-02-26 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0016_order_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_Id',
            new_name='order_id',
        ),
    ]