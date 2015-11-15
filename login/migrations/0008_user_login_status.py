# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20151115_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_login',
            name='Status',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
