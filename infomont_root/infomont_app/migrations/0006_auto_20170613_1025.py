# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomont_app', '0005_auto_20170613_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layoutcampo',
            name='etichetta',
            field=models.CharField(max_length=200, verbose_name='Etichetta'),
        ),
    ]