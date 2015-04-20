# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0003_newhouse_metro3'),
    ]

    operations = [
        migrations.AddField(
            model_name='newhouse',
            name='cmsa',
            field=models.CharField(max_length=2, null=True, db_column=b'CMSA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fmr',
            field=models.PositiveIntegerField(null=True, db_column=b'FMR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fmra',
            field=models.PositiveIntegerField(null=True, db_column=b'FMRA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='fmrb',
            field=models.PositiveIntegerField(null=True, db_column=b'FMRB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='histry',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'HISTRY'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='ipov',
            field=models.PositiveIntegerField(null=True, db_column=b'IPOV'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l30',
            field=models.PositiveIntegerField(null=True, db_column=b'L30'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l30a',
            field=models.PositiveIntegerField(null=True, db_column=b'L30A'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l30b',
            field=models.PositiveIntegerField(null=True, db_column=b'L30B'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l50',
            field=models.PositiveIntegerField(null=True, db_column=b'L50'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l50a',
            field=models.PositiveIntegerField(null=True, db_column=b'L50A'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l50b',
            field=models.PositiveIntegerField(null=True, db_column=b'L50B'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l80',
            field=models.PositiveIntegerField(null=True, db_column=b'L80'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l80a',
            field=models.PositiveIntegerField(null=True, db_column=b'L80A'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='l80b',
            field=models.PositiveIntegerField(null=True, db_column=b'L80B'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='lmed',
            field=models.PositiveIntegerField(null=True, db_column=b'LMED'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='lmeda',
            field=models.PositiveIntegerField(null=True, db_column=b'LMEDA'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='lmedb',
            field=models.PositiveIntegerField(null=True, db_column=b'LMEDB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='region',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'REGION'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='smsa',
            field=models.CharField(max_length=4, null=True, db_column=b'SMSA'),
        ),
    ]
