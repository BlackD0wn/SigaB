# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0010_auto_20180413_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='matricula',
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frequencia', to='frequencia.Materia'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='presente',
            field=models.BooleanField(default=False),
        ),
    ]
