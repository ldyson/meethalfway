# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halfwayapp', '0016_auto_20160225_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='business_type',
            field=models.CharField(blank=True, choices=[(b'Coffee', b'Coffee Shop'), (b'Bar', b'Bar'), (b'Eatery', b'Restaurant')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='transit_mode',
            field=models.CharField(choices=[(b'Walk', b'Walking'), (b'Public Transit', b'Public Transit'), (b'Car', b'Driving')], max_length=70),
        ),
    ]