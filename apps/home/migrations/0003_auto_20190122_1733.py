# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-22 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190121_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='band_name',
            new_name='brand_name',
        ),
        migrations.RemoveField(
            model_name='goodsdetail',
            name='desc',
        ),
    ]
