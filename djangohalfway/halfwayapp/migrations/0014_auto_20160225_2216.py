# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halfwayapp', '0013_auto_20160225_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='transit_mode',
            field=models.CharField(max_length=70),
        ),
    ]
