# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomont_app', '0003_auto_20170613_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='layoutcampo',
            name='in_alto',
            field=models.BooleanField(default=False, verbose_name='Presente nella barra riassuntiva'),
        ),
    ]