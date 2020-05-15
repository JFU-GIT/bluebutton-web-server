# Generated by Django 2.1.11 on 2019-12-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluebutton', '0002_auto_20180127_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crosswalk',
            name='fhir_id',
            field=models.CharField(db_column='fhir_id', db_index=True, default=None, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='crosswalk',
            name='user_id_hash',
            field=models.CharField(db_column='user_id_hash', db_index=True, default=None, max_length=64, unique=True, verbose_name='PBKDF2 of User ID'),
        ),
        migrations.RenameField(
            model_name='crosswalk',
            old_name='fhir_id',
            new_name='_fhir_id',
        ),
        migrations.RenameField(
            model_name='crosswalk',
            old_name='user_id_hash',
            new_name='_user_id_hash',
        ),
    ]