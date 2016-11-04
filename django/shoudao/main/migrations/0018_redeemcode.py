# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-29 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedeemCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('item', models.CharField(max_length=20)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
    ]