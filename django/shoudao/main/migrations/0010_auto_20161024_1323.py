# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20161024_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='expiration',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='type',
            field=models.CharField(default='普通账户', max_length=20),
        ),
    ]
