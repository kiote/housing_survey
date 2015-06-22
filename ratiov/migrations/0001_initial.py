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
                ('rcarp', models.SmallIntegerField(null=True, db_column=b'RCARP')),
                ('rclot', models.SmallIntegerField(null=True, db_column=b'RCLOT')),
                ('rcost', models.SmallIntegerField(null=True, db_column=b'RCOST')),
                ('rgroc', models.SmallIntegerField(null=True, db_column=b'RGROC')),
                ('rkidc', models.SmallIntegerField(null=True, db_column=b'RKIDC')),
                ('rmedi', models.SmallIntegerField(null=True, db_column=b'RMEDI')),
                ('rothe', models.SmallIntegerField(null=True, db_column=b'ROTHE')),
                ('rutil', models.SmallIntegerField(null=True, db_column=b'RUTIL')),
                ('field_in_2013', models.BooleanField(default=False)),
                ('field_in_2011', models.BooleanField(default=False)),
                ('export_year', models.PositiveSmallIntegerField(null=True, db_index=True)),
            ],
            options={
                'db_table': 'ahs_ratiov',
            },
        ),
        migrations.AlterIndexTogether(
            name='ratiov',
            index_together=set([('control', 'export_year'), ('field_in_2013', 'field_in_2011')]),
        ),
    ]
