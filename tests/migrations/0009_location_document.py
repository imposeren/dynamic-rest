# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-26 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_officer'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='document',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
