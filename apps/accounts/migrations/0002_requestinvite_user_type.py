# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestinvite',
            name='user_type',
            field=models.CharField(choices=[('BEN', 'Beneficiary'), ('DEV', 'Developer')], default='BEN', max_length=5),
        ),
    ]
