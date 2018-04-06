# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-06 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('sales_count', models.PositiveSmallIntegerField(default=1)),
                ('sell_price', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_size', models.CharField(choices=[('F', 'FREE'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('X', 'XL')], max_length=1)),
                ('pants_size', models.CharField(choices=[('F', 'FREE'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('X', 'XL'), ('Z', '2XL'), ('B', '3XL')], max_length=1)),
                ('type', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
