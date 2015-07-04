# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rmov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('control', models.BigIntegerField(null=True, db_column=b'CONTROL')),
                ('dbinreas', models.SmallIntegerField(null=True, db_column=b'DBINREAS')),
                ('dbinvol', models.SmallIntegerField(null=True, db_column=b'DBINVOL')),
                ('dbinwher', models.SmallIntegerField(null=True, db_column=b'DBINWHER')),
                ('dbinwhy', models.SmallIntegerField(null=True, db_column=b'DBINWHY')),
                ('jdbinreas', models.SmallIntegerField(null=True, db_column=b'JDBINREAS')),
                ('jdbinvol', models.SmallIntegerField(null=True, db_column=b'JDBINVOL')),
                ('jdbinwher', models.SmallIntegerField(null=True, db_column=b'JDBINWHER')),
                ('jdbinwhy', models.SmallIntegerField(null=True, db_column=b'JDBINWHY')),
                ('jovgrp', models.SmallIntegerField(null=True, db_column=b'JOVGRP')),
                ('jxhead', models.SmallIntegerField(null=True, db_column=b'JXHEAD')),
                ('jxper', models.SmallIntegerField(null=True, db_column=b'JXPER')),
                ('jxten', models.SmallIntegerField(null=True, db_column=b'JXTEN')),
                ('jxunit', models.SmallIntegerField(null=True, db_column=b'JXUNIT')),
                ('movgrp', models.PositiveSmallIntegerField(null=True, db_column=b'MOVGRP')),
                ('mvg', models.PositiveSmallIntegerField(null=True, db_column=b'MVG')),
                ('rmov', models.SmallIntegerField(null=True, db_column=b'RMOV')),
                ('xcond', models.SmallIntegerField(null=True, db_column=b'XCOND')),
                ('xcoop', models.SmallIntegerField(null=True, db_column=b'XCOOP')),
                ('xcost', models.SmallIntegerField(null=True, db_column=b'XCOST')),
                ('xhead', models.SmallIntegerField(null=True, db_column=b'XHEAD')),
                ('xinus', models.SmallIntegerField(null=True, db_column=b'XINUS')),
                ('xper', models.SmallIntegerField(null=True, db_column=b'XPER')),
                ('xrel', models.SmallIntegerField(null=True, db_column=b'XREL')),
                ('xten', models.SmallIntegerField(null=True, db_column=b'XTEN')),
                ('xunit', models.SmallIntegerField(null=True, db_column=b'XUNIT')),
                ('field_in_2013', models.BooleanField(default=False)),
                ('field_in_2011', models.BooleanField(default=False)),
                ('export_year', models.PositiveSmallIntegerField(null=True, db_index=True)),
            ],
            options={
                'db_table': 'ahs_rmov',
            },
        ),
        migrations.AlterIndexTogether(
            name='rmov',
            index_together=set([('control', 'export_year'), ('field_in_2013', 'field_in_2011')]),
        ),
    ]
