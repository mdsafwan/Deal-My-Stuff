# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20151114_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='Mobile_Number',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
