# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 01:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inflacionThomsonReuters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.FloatField(default=0)),
                ('fecha', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
