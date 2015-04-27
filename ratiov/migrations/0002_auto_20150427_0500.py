# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratiov', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratiov',
            name='control',
            field=models.BigIntegerField(unique=True, serialize=False, primary_key=True, db_column=b'CONTROL'),
        ),
    ]
