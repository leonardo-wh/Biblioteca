# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2022-09-22 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('editor', '0001_initial'),
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField(blank=True, null=True)),
                ('portada', models.ImageField(upload_to='portadas')),
                ('autores', models.ManyToManyField(to='autor.Autor')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.Editor')),
            ],
        ),
    ]
