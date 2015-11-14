# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20151113_1545'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_details',
            options={'ordering': ['pk'], 'managed': True},
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_details',
            name='User_ID',
            field=models.CharField(default=b'DMS_0000', max_length=8, serialize=False, primary_key=True),
        ),
    ]
