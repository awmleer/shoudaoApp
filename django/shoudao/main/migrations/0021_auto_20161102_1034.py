# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-02 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_redeemcode_who_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='expiration',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
