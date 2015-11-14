# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20151114_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='advertisement',
            fields=[
                ('Advertisement_ID', models.CharField(default=b'ADV_0000', max_length=8, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=100, null=True, blank=True)),
                ('Post_Date', models.DateTimeField(null=True, blank=True)),
                ('Sold_Date', models.DateTimeField(null=True, blank=True)),
                ('Status', models.CharField(max_length=10, null=True, blank=True)),
                ('MRP', models.IntegerField(null=True, blank=True)),
                ('Selling_Price', models.IntegerField(null=True, blank=True)),
                ('Advertisement_Tag1', models.CharField(max_length=50, null=True, blank=True)),
                ('Advertisement_Tag2', models.CharField(max_length=50, null=True, blank=True)),
                ('Advertisement_Tag3', models.CharField(max_length=50, null=True, blank=True)),
                ('Description', models.TextField(null=True, blank=True)),
                ('Buyer_User_ID', models.ForeignKey(related_name='Buyer_User_ID', to='login.user_details')),
                ('Seller_User_ID', models.ForeignKey(related_name='Seller_User_ID', to='login.user_details')),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Product_ID', models.CharField(max_length=8, null=True, blank=True)),
                ('Category', models.CharField(max_length=16, null=True, blank=True)),
                ('Advertisement_ID', models.ForeignKey(to='advertisements.advertisement')),
            ],
        ),
    ]
