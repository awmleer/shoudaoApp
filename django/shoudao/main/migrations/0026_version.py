# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-15 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20161115_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=15)),
                ('major', models.SmallIntegerField()),
                ('minor', models.SmallIntegerField()),
                ('revision', models.SmallIntegerField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
