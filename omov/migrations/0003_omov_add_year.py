# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omov', '0002_remove_omov_smsa'),
    ]

    operations = [
        migrations.AddField(
            model_name='omov',
            name='add_year',
            field=models.PositiveSmallIntegerField(default=2013, db_column=b'ADD_YEAR', db_index=True),
        ),
    ]
