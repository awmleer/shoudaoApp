# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-28 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20161026_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagedatanotice',
            name='buttons',
            field=models.CharField(default='[]', max_length=500),
        ),
    ]
