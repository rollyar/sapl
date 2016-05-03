# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0012_auto_20160309_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculonormajuridica',
            name='norma_referente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='norma_referente_set', to='norma.NormaJuridica'),
        ),
        migrations.AlterField(
            model_name='vinculonormajuridica',
            name='norma_referida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='norma_referida_set', to='norma.NormaJuridica'),
        ),
    ]
