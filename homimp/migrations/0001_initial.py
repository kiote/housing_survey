# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homimp',
            fields=[
                ('control', models.BigIntegerField(unique=True, serialize=False, primary_key=True, db_column=b'CONTROL')),
                ('rad', models.IntegerField(null=True, db_column=b'RAD')),
                ('smsa', models.PositiveIntegerField(null=True, db_column=b'SMSA')),
                ('rah', models.PositiveSmallIntegerField(null=True, db_column=b'RAH')),
                ('jrad', models.SmallIntegerField(null=True, db_column=b'JRAD')),
                ('ras', models.PositiveSmallIntegerField(null=True, db_column=b'RAS')),
                ('jras', models.SmallIntegerField(null=True, db_column=b'JRAS')),
            ],
        ),
    ]
