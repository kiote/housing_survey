# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratiov', '0002_remove_ratiov_smsa'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratiov',
            name='add_year',
            field=models.PositiveSmallIntegerField(default=2013, db_column=b'ADD_YEAR', db_index=True),
        ),
    ]
