# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-03 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Neibas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neiba',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
