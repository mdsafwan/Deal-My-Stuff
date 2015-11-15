# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0005_auto_20151115_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['pk'], 'managed': True, 'verbose_name_plural': 'advertisements'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'books'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'managed': True, 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='electronic_gadget',
            options={'verbose_name_plural': 'electronic_gadgets'},
        ),
        migrations.AlterModelOptions(
            name='household_item',
            options={'verbose_name_plural': 'household_items'},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'verbose_name_plural': 'vehicles'},
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisement',
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='electronic_gadget',
            table='electronic_gadget',
        ),
        migrations.AlterModelTable(
            name='household_item',
            table='household_item',
        ),
        migrations.AlterModelTable(
            name='vehicle',
            table='vehicle',
        ),
    ]
