# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 23:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweetsubs', '0002_auto_20171106_2333'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newsletters',
            new_name='Newsletter',
        ),
    ]
