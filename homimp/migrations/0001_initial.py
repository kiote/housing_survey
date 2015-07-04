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
                ('control', models.BigIntegerField(null=True, db_column=b'CONTROL')),
                ('jrad', models.SmallIntegerField(null=True, db_column=b'JRAD')),
                ('jras', models.SmallIntegerField(null=True, db_column=b'JRAS')),
                ('rad', models.IntegerField(null=True, db_column=b'RAD')),
                ('rah', models.SmallIntegerField(null=True, db_column=b'RAH')),
                ('rahk', models.SmallIntegerField(null=True, db_column=b'RAHK')),
                ('ras', models.PositiveSmallIntegerField(null=True, db_column=b'RAS')),
                ('field_in_2013', models.BooleanField(default=False)),
                ('field_in_2011', models.BooleanField(default=False)),
                ('export_year', models.PositiveSmallIntegerField(null=True, db_index=True)),
            ],
            options={
                'db_table': 'ahs_homimp',
            },
        ),
        migrations.AlterIndexTogether(
            name='homimp',
            index_together=set([('control', 'export_year'), ('field_in_2013', 'field_in_2011')]),
        ),
    ]
