# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_article_imgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dimDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
