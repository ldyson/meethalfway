# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_type', models.TextField()),
                ('trip_id', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halfwayapp.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transit_mode', models.TextField(max_length=70)),
                ('starting_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halfwayapp.Address')),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='participant_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Participant_one', to='halfwayapp.Participant'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='participant_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Participant_two', to='halfwayapp.Participant'),
        ),
    ]
