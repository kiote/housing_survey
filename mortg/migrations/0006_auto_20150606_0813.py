# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortg', '0005_mortg_add_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='mortg',
            name='hemnmor',
            field=models.SmallIntegerField(null=True, db_column=b'HEMNMOR'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='hemnmor2',
            field=models.SmallIntegerField(null=True, db_column=b'HEMNMOR2'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='mnmor',
            field=models.SmallIntegerField(null=True, db_column=b'MNMOR'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='mnmor2',
            field=models.SmallIntegerField(null=True, db_column=b'MNMOR2'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='mnmor3',
            field=models.SmallIntegerField(null=True, db_column=b'MNMOR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ammrt4',
            field=models.IntegerField(null=True, db_column=b'AMMRT4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='amtm3',
            field=models.IntegerField(null=True, db_column=b'AMTM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='mxdjtm',
            field=models.IntegerField(null=True, db_column=b'MXDJTM'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='orintr3',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'ORINTR3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmt4',
            field=models.IntegerField(null=True, db_column=b'PMT4'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='ptcham3',
            field=models.IntegerField(null=True, db_column=b'PTCHAM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='unpbal4',
            field=models.IntegerField(null=True, db_column=b'UNPBAL4'),
        ),
    ]
