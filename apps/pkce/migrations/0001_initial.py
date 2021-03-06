# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-26 21:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from oauth2_provider import settings as oauth2_settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(oauth2_settings.GRANT_MODEL)
    ]

    operations = [
        migrations.CreateModel(
            name='CodeChallenge',
            fields=[
                ('grant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=oauth2_settings.GRANT_MODEL)),
                ('challenge', models.CharField(max_length=255)),
                ('challenge_method', models.CharField(default='S256', max_length=255)),
            ],
        ),
    ]
