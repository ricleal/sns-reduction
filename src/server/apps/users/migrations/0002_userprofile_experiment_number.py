# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='experiment_number',
            field=models.IntegerField(default=0, help_text='HFIR Experiment Number (expXXX)'),
        ),
    ]