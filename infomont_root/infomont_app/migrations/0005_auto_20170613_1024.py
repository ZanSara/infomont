# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomont_app', '0004_layoutcampo_in_alto'),
    ]

    operations = [
        migrations.AddField(
            model_name='layoutcampo',
            name='etichetta',
            field=models.CharField(default='etichetta', max_length=200, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='commisione',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Commissione Regionale'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='compentenza',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Ente Sovracomunale di Competenza'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='comprensorio',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Comprensorio Sciistico'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='comune',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Comune'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='gruppo',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Gruppo Montuoso'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='localita',
            field=models.CharField(default='<Vuoto>', max_length=800, verbose_name='Località'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='nome',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='provincia',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Provincia'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='regione',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Regione'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='sezione',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Sezione'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='sito',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Sito Web'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='valle',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Valle'),
        ),
        migrations.AlterField(
            model_name='rifugio',
            name='zona_tutelata',
            field=models.CharField(default='<Vuoto>', max_length=200, verbose_name='Zona Tutelata'),
        ),
    ]