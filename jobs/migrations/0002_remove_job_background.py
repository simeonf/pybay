# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2019-03-14 02:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='background',
        ),
    ]
