# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('control', models.BigIntegerField(unique=True, serialize=False, primary_key=True, db_column=b'CONTROL')),
                ('smsa', models.PositiveIntegerField(null=True, db_column=b'SMSA')),
                ('jwnher', models.SmallIntegerField(null=True, db_column=b'JWNHER')),
                ('ownhere', models.SmallIntegerField(null=True, db_column=b'OWNHERE')),
            ],
        ),
    ]
