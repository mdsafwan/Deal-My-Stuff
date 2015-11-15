# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0006_auto_20151115_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='Buyer_User_ID',
            field=models.ForeignKey(related_name='Buyer_User_ID', db_column=b'Buyer_User_ID', to='login.user_details'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='Seller_User_ID',
            field=models.ForeignKey(related_name='Seller_User_ID', db_column=b'Seller_User_ID', to='login.user_details'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Product_ID',
            field=models.ForeignKey(to='advertisements.category', db_column=b'Product_ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='Advertisement_ID',
            field=models.ForeignKey(to='advertisements.advertisement', db_column=b'Advertisement_ID'),
        ),
        migrations.AlterField(
            model_name='electronic_gadget',
            name='Product_ID',
            field=models.ForeignKey(to='advertisements.category', db_column=b'Product_ID'),
        ),
        migrations.AlterField(
            model_name='household_item',
            name='Product_ID',
            field=models.ForeignKey(to='advertisements.category', db_column=b'Product_ID'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='Product_ID',
            field=models.ForeignKey(to='advertisements.category', db_column=b'Product_ID'),
        ),
    ]
