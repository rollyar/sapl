# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 20:53
from __future__ import unicode_literals

from django.db import migrations, models
import sapl.materia.models
import sapl.utils


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0038_auto_20160612_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposicao',
            name='data_devolucao',
        ),
        migrations.AddField(
            model_name='proposicao',
            name='data_incorporação',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Incorporação'),
        ),
        migrations.AlterField(
            model_name='proposicao',
            name='data_recebimento',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Recebimento'),
        ),
        migrations.AlterField(
            model_name='proposicao',
            name='status',
            field=models.CharField(blank=True, choices=[('E', 'Enviada'), ('R', 'Recebida'), ('I', 'Incorporada')], max_length=1, verbose_name='Status Proposição'),
        ),
        migrations.AlterField(
            model_name='proposicao',
            name='texto_original',
            field=models.FileField(default='', upload_to=sapl.materia.models.texto_upload_path, validators=[sapl.utils.restringe_tipos_de_arquivo_txt], verbose_name='Texto Original'),
            preserve_default=False,
        ),
    ]
