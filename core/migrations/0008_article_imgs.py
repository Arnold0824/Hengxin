# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170321_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imgs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.picture'),
        ),
    ]
