# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_remove_owner_smsa'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='add_year',
            field=models.PositiveSmallIntegerField(default=2013, db_column=b'ADD_YEAR', db_index=True),
        ),
    ]
