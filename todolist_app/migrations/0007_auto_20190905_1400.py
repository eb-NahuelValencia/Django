# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-05 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0006_auto_20190902_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id_event',
            field=models.CharField(max_length=30),
        ),
    ]