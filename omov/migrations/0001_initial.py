# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Omov',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('control', models.BigIntegerField(null=True, db_column=b'CONTROL', db_index=True)),
                ('dbgrpcnt', models.PositiveSmallIntegerField(null=True, db_column=b'DBGRPCNT')),
                ('dboutlen', models.SmallIntegerField(null=True, db_column=b'DBOUTLEN')),
                ('dboutreas', models.SmallIntegerField(null=True, db_column=b'DBOUTREAS')),
                ('dboutvol', models.SmallIntegerField(null=True, db_column=b'DBOUTVOL')),
                ('dboutwher', models.SmallIntegerField(null=True, db_column=b'DBOUTWHER')),
                ('dboutwhy', models.SmallIntegerField(null=True, db_column=b'DBOUTWHY')),
                ('dbugroup', models.PositiveSmallIntegerField(null=True, db_column=b'DBUGROUP')),
                ('field_in_2013', models.BooleanField(default=False)),
                ('field_in_2011', models.BooleanField(default=False)),
                ('export_year', models.PositiveSmallIntegerField(null=True, db_index=True)),
            ],
            options={
                'db_table': 'ahs_omov',
            },
        ),
        migrations.AlterIndexTogether(
            name='omov',
            index_together=set([('control', 'export_year'), ('field_in_2013', 'field_in_2011')]),
        ),
    ]
