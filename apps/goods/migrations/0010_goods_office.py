# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-10-03 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0006_auto_20201003_2013'),
        ('goods', '0009_remove_goodscategory_is_tab'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='office',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_operation.Office', verbose_name='处室名称'),
        ),
    ]
