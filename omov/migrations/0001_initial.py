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
                ('control', models.BigIntegerField(unique=True, serialize=False, primary_key=True, db_column=b'CONTROL')),
                ('smsa', models.PositiveIntegerField(null=True, db_column=b'SMSA')),
                ('dboutreas', models.SmallIntegerField(null=True, db_column=b'DBOUTREAS')),
                ('dboutlen', models.SmallIntegerField(null=True, db_column=b'DBOUTLEN')),
                ('dbgrpcnt', models.PositiveSmallIntegerField(null=True, db_column=b'DBGRPCNT')),
                ('dboutvol', models.SmallIntegerField(null=True, db_column=b'DBOUTVOL')),
                ('dbugroup', models.PositiveSmallIntegerField(null=True, db_column=b'DBUGROUP')),
                ('dboutwhy', models.SmallIntegerField(null=True, db_column=b'DBOUTWHY')),
                ('dboutwher', models.SmallIntegerField(null=True, db_column=b'DBOUTWHER')),
            ],
        ),
    ]
