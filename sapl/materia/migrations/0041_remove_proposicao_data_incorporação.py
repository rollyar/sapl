# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-10 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0040_auto_20160810_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposicao',
            name='data_incorporação',
        ),
    ]
