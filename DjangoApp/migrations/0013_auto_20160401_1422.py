# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 14:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0012_auto_20160401_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('can_deliver_pizzas', 'Can deliver pizzas'),)},
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 14, 22, 14, 665140)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 14, 22, 14, 666117)),
        ),
    ]