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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('control', models.BigIntegerField(db_column=b'CONTROL', db_index=True)),
                ('jwnher', models.SmallIntegerField(null=True, db_column=b'JWNHER')),
                ('ownhere', models.SmallIntegerField(null=True, db_column=b'OWNHERE')),
                ('export_year', models.PositiveSmallIntegerField(null=True, db_index=True)),
            ],
            options={
                'db_table': 'ahs_owner',
            },
        ),
        migrations.AlterIndexTogether(
            name='owner',
            index_together=set([('control', 'export_year')]),
        ),
    ]
