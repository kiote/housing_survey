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
                ('control', models.BigIntegerField(unique=True, serialize=False, primary_key=True, db_column=b'CONTROL')),
                ('jdbinreas', models.SmallIntegerField(null=True, db_column=b'JDBINREAS')),
                ('dbinwhy', models.SmallIntegerField(null=True, db_column=b'DBINWHY')),
                ('xunit', models.SmallIntegerField(null=True, db_column=b'XUNIT')),
                ('jxunit', models.SmallIntegerField(null=True, db_column=b'JXUNIT')),
                ('xcoop', models.SmallIntegerField(null=True, db_column=b'XCOOP')),
                ('jxper', models.SmallIntegerField(null=True, db_column=b'JXPER')),
                ('smsa', models.PositiveIntegerField(null=True, db_column=b'SMSA')),
                ('dbinreas', models.SmallIntegerField(null=True, db_column=b'DBINREAS')),
                ('dbinwher', models.SmallIntegerField(null=True, db_column=b'DBINWHER')),
                ('dbinvol', models.SmallIntegerField(null=True, db_column=b'DBINVOL')),
                ('xcond', models.SmallIntegerField(null=True, db_column=b'XCOND')),
                ('jxten', models.SmallIntegerField(null=True, db_column=b'JXTEN')),
                ('jdbinwhy', models.SmallIntegerField(null=True, db_column=b'JDBINWHY')),
                ('mvg', models.PositiveSmallIntegerField(null=True, db_column=b'MVG')),
                ('jdbinwher', models.SmallIntegerField(null=True, db_column=b'JDBINWHER')),
                ('xcost', models.SmallIntegerField(null=True, db_column=b'XCOST')),
                ('jxhead', models.SmallIntegerField(null=True, db_column=b'JXHEAD')),
                ('jovgrp', models.SmallIntegerField(null=True, db_column=b'JOVGRP')),
                ('xrel', models.SmallIntegerField(null=True, db_column=b'XREL')),
                ('xhead', models.SmallIntegerField(null=True, db_column=b'XHEAD')),
                ('xper', models.SmallIntegerField(null=True, db_column=b'XPER')),
                ('xten', models.SmallIntegerField(null=True, db_column=b'XTEN')),
                ('jdbinvol', models.SmallIntegerField(null=True, db_column=b'JDBINVOL')),
            ],
        ),
    ]
