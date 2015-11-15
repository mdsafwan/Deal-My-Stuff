# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_book_electronic_gadget_household_item_vehicle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Language',
            new_name='Book_Language',
        ),
    ]
