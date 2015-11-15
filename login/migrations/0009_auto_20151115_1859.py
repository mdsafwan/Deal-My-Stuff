# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_user_login_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_login',
            name='User_ID',
            field=models.ForeignKey(related_name='User_ID_Loggedin', db_column=b'User_ID', to='login.user_details'),
        ),
    ]
