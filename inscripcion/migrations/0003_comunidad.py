# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-03 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0002_catequista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id_comunidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
    ]
