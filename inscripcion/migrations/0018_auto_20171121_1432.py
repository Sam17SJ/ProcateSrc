# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0017_auto_20171121_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catequista',
            name='id_comunidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inscripcion.Comunidad'),
        ),
        migrations.AlterField(
            model_name='catequista',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
