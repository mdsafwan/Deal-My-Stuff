# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_advertisement_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Genre', models.CharField(max_length=100, null=True, blank=True)),
                ('Language', models.CharField(max_length=100, null=True, blank=True)),
                ('Publisher', models.CharField(max_length=100, null=True, blank=True)),
                ('Product_ID', models.ForeignKey(to='advertisements.category')),
            ],
        ),
        migrations.CreateModel(
            name='electronic_gadget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Brand', models.CharField(max_length=100, null=True, blank=True)),
                ('Product_Model', models.CharField(max_length=100, null=True, blank=True)),
                ('Specification', models.TextField(null=True, blank=True)),
                ('Product_ID', models.ForeignKey(to='advertisements.category')),
            ],
        ),
        migrations.CreateModel(
            name='household_item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Brand', models.CharField(max_length=100, null=True, blank=True)),
                ('Type', models.CharField(max_length=100, null=True, blank=True)),
                ('Product_ID', models.ForeignKey(to='advertisements.category')),
            ],
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Manufacturer', models.CharField(max_length=100, null=True, blank=True)),
                ('Product_Model', models.CharField(max_length=100, null=True, blank=True)),
                ('Year', models.CharField(max_length=4, null=True, blank=True)),
                ('Product_ID', models.ForeignKey(to='advertisements.category')),
            ],
        ),
    ]
