# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.email_null
import profiles.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temp_key', models.CharField(max_length=100, verbose_name='temp_key')),
                ('timestamp', models.DateTimeField(default=profiles.models.now, verbose_name='timestamp')),
                ('reset', models.BooleanField(default=False, verbose_name='reset yet?')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'password reset',
                'verbose_name_plural': 'password resets',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_email', profiles.email_null.EmailNullField(max_length=254, unique=True, null=True, blank=True)),
                ('phone', models.CharField(help_text='Telefono', max_length=20, null=True, verbose_name='Telefono', blank=True)),
                ('publish_phone', models.BooleanField(default=False)),
                ('publish_email', models.BooleanField(default=True)),
                ('notify_wishlist', models.BooleanField(default=False)),
                ('notify_added_books', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
