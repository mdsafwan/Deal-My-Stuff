# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User_ID', models.CharField(max_length=8, null=True, blank=True)),
                ('User_Name', models.CharField(max_length=20, unique=True, null=True, blank=True)),
                ('Name', models.CharField(max_length=20, null=True, blank=True)),
                ('USN', models.CharField(max_length=10, null=True, blank=True)),
                ('Email', models.EmailField(max_length=20, null=True, blank=True)),
                ('Mobile_Number', models.BigIntegerField(null=True, blank=True)),
                ('Address', models.TextField(null=True, blank=True)),
                ('Password', models.CharField(max_length=16, null=True, blank=True)),
                ('abcd', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'user_details',
                'managed': True,
            },
        ),
    ]
