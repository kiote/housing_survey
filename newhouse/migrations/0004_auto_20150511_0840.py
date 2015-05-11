# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0003_auto_20150429_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='cmsa',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'CMSA', db_index=True),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='division',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'DIVISION', db_index=True),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='metro3',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'METRO3', db_index=True),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='region',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'REGION', db_index=True),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='smsa',
            field=models.PositiveIntegerField(null=True, db_column=b'SMSA', db_index=True),
        ),
    ]
