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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('control', models.BigIntegerField(null=True, db_column=b'CONTROL', db_index=True)),
                ('rad', models.IntegerField(null=True, db_column=b'RAD')),
                ('smsa', models.PositiveIntegerField(null=True, db_column=b'SMSA', db_index=True)),
                ('rah', models.PositiveSmallIntegerField(null=True, db_column=b'RAH')),
                ('jrad', models.SmallIntegerField(null=True, db_column=b'JRAD')),
                ('ras', models.PositiveSmallIntegerField(null=True, db_column=b'RAS')),
                ('jras', models.SmallIntegerField(null=True, db_column=b'JRAS')),
            ],
            options={
                'db_table': 'ahs_homimp',
            },
        ),
    ]
