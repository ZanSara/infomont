# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomont_app', '0010_auto_20170613_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rifugio',
            name='categoria_cai',
            field=models.CharField(choices=[('E', 'Escursionistico'), ('A', 'Aplinistico')], default='E', max_length=15, verbose_name='Categoria CAI'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='tipo_rifugio',
            field=models.CharField(choices=[('Custodito', 'Custodito'), ('Bivacco', 'Bivacco'), ('Stagionale', 'Stagionale')], default='Bivacco', max_length=15, verbose_name='Tipo Rifugio'),
        ),
    ]