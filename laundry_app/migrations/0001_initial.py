# Generated by Django 3.2.1 on 2024-02-05 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ClotheType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('number', models.CharField(max_length=20, verbose_name='number')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, verbose_name='number')),
                ('action', models.ManyToManyField(blank=True, to='laundry_app.Action')),
                ('cloth', models.ManyToManyField(blank=True, to='laundry_app.ClotheType')),
            ],
        ),
    ]
