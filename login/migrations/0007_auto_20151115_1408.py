# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20151115_1149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_login',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='user_login',
            table='user_login',
        ),
    ]
