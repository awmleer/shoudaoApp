# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161022_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='main.Message'),
        ),
    ]
