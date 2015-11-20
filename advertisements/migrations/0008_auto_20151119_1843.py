# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0007_auto_20151115_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Category_ID', models.CharField(max_length=8, null=True, blank=True)),
                ('Category', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'category_type',
                'verbose_name_plural': 'category_type',
            },
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='Buyer_User_ID',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='Sold_Date',
        ),
    ]
