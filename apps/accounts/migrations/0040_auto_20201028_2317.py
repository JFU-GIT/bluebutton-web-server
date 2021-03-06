# Generated by Django 2.2.13 on 2020-10-28 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0039_auto_20190814_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastPassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(editable=False, max_length=255, verbose_name='Password Hash')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
            options={
                'verbose_name': 'Past Password',
                'verbose_name_plural': 'Past Passwords',
                'ordering': ['-userpassword_desc', 'password'],
            },
        ),
        migrations.CreateModel(
            name='UserPasswordDescriptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Descriptor Created On')),
                ('salt', models.CharField(editable=False, max_length=120, verbose_name='Salt')),
                ('iterations', models.IntegerField(blank=True, default=None, editable=False, null=True, verbose_name='Iterations')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Password Descriptor',
                'verbose_name_plural': 'Password Descriptors',
                'ordering': ['-user', 'iterations'],
                'unique_together': {('user', 'iterations')},
            },
        ),
        migrations.AddField(
            model_name='pastpassword',
            name='userpassword_desc',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserPasswordDescriptor'),
        ),
        migrations.AlterUniqueTogether(
            name='pastpassword',
            unique_together={('userpassword_desc', 'password', 'date_created')},
        ),
    ]
