# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ratiov',
            fields=[
                ('control', models.BigIntegerField(unique=True, serialize=False, primary_key=True, db_column=b'CONTROL')),
                ('rgroc', models.SmallIntegerField(null=True, db_column=b'RGROC')),
                ('rmedi', models.SmallIntegerField(null=True, db_column=b'RMEDI')),
                ('smsa', models.PositiveIntegerField(null=True, db_column=b'SMSA', db_index=True)),
                ('rcarp', models.SmallIntegerField(null=True, db_column=b'RCARP')),
                ('rutil', models.SmallIntegerField(null=True, db_column=b'RUTIL')),
                ('rcost', models.SmallIntegerField(null=True, db_column=b'RCOST')),
                ('rclot', models.SmallIntegerField(null=True, db_column=b'RCLOT')),
                ('rkidc', models.SmallIntegerField(null=True, db_column=b'RKIDC')),
                ('rothe', models.SmallIntegerField(null=True, db_column=b'ROTHE')),
            ],
            options={
                'db_table': 'ahs_ratiov',
            },
        ),
    ]
