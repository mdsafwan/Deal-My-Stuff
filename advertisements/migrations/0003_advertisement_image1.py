# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_auto_20151114_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='Image1',
            field=models.TextField(null=True, blank=True),
        ),
    ]
