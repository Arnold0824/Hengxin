# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 08:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170316_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carousel',
            old_name='img',
            new_name='imgs',
        ),
    ]