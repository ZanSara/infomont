# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomont_app', '0008_auto_20170613_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina',
            name='glyph',
            field=models.CharField(default='chevron-left', max_length=50, verbose_name='Glifo Pagina'),
            preserve_default=False,
        ),
    ]