# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=2000)),
                ('can_buy', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('footer', models.CharField(max_length=500)),
                ('footer_style', models.CharField(max_length=30)),
            ],
        ),
    ]
