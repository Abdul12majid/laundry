# Generated by Django 4.0.3 on 2024-02-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0015_action_order_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
