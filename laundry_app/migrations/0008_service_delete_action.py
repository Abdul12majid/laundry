# Generated by Django 4.0.3 on 2024-02-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0007_order_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Action',
        ),
    ]
