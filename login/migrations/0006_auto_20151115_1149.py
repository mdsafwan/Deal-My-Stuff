# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20151114_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Logged_In_Time', models.DateTimeField(null=True, blank=True)),
                ('Logged_Out_Time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='user_details',
            options={'ordering': ['pk'], 'managed': True, 'verbose_name_plural': 'user_details'},
        ),
        migrations.AddField(
            model_name='user_login',
            name='User_ID',
            field=models.ForeignKey(related_name='User_ID_Loggedin', to='login.user_details'),
        ),
    ]
