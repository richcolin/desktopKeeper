# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-10-03 20:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_auto_20201003_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategory',
            name='is_tab',
        ),
    ]