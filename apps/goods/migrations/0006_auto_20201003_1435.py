# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-10-03 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20201002_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.IntegerField(choices=[(1, '台式机'), (2, '笔记本电脑'), (3, '平板电脑'), (4, '路由器'), (5, '交换机'), (6, '其他')], help_text='类目级别', verbose_name='类目级别'),
        ),
    ]
