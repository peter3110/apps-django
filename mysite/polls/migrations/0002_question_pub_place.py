# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_place',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
