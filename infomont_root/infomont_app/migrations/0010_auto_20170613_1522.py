# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomont_app', '0009_pagina_glyph'),
    ]

    operations = [
        migrations.AddField(
            model_name='rifugio',
            name='latitudine',
            field=models.DecimalField(decimal_places=6, default=46.3093808, max_digits=9, verbose_name='Latitudine'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rifugio',
            name='longitudine',
            field=models.DecimalField(decimal_places=6, default=9.7374249, max_digits=9, verbose_name='Longitudine'),
            preserve_default=False,
        ),
    ]
