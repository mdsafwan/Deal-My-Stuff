# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_user_details_ab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='ab',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='abcd',
        ),
    ]
