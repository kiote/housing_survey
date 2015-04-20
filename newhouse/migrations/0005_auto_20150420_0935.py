# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0004_auto_20150420_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='newhouse',
            name='amte',
            field=models.PositiveIntegerField(null=True, db_column=b'AMTE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='amtg',
            field=models.PositiveIntegerField(null=True, db_column=b'AMTG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='baths',
            field=models.CharField(max_length=2, null=True, db_column=b'BATHS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='bedrms',
            field=models.CharField(max_length=2, null=True, db_column=b'BEDRMS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='burner',
            field=models.CharField(max_length=2, null=True, db_column=b'BURNER'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='buye',
            field=models.CharField(max_length=2, null=True, db_column=b'BUYE'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='buyg',
            field=models.CharField(max_length=2, null=True, db_column=b'BUYG'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='cook',
            field=models.CharField(max_length=2, null=True, db_column=b'COOK'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dens',
            field=models.CharField(max_length=2, null=True, db_column=b'DENS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dining',
            field=models.CharField(max_length=2, null=True, db_column=b'DINING'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dish',
            field=models.CharField(max_length=2, null=True, db_column=b'DISH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='division',
            field=models.CharField(max_length=2, null=True, db_column=b'DIVISION'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='dry',
            field=models.CharField(max_length=2, null=True, db_column=b'DRY'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='famrm',
            field=models.CharField(max_length=2, null=True, db_column=b'FAMRM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='gaspip',
            field=models.CharField(max_length=2, null=True, db_column=b'GASPIP'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='halfb',
            field=models.CharField(max_length=2, null=True, db_column=b'HALFB'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='hfuel',
            field=models.CharField(max_length=2, null=True, db_column=b'HFUEL'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='kitch',
            field=models.CharField(max_length=2, null=True, db_column=b'KITCH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='living',
            field=models.CharField(max_length=2, null=True, db_column=b'LIVING'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='nunit2',
            field=models.CharField(max_length=2, null=True, db_column=b'NUNIT2'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='othfn',
            field=models.CharField(max_length=2, null=True, db_column=b'OTHFN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='oven',
            field=models.CharField(max_length=2, null=True, db_column=b'OVEN'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='recrm',
            field=models.CharField(max_length=2, null=True, db_column=b'RECRM'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='refr',
            field=models.CharField(max_length=2, null=True, db_column=b'REFR'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='usegas',
            field=models.CharField(max_length=2, null=True, db_column=b'USEGAS'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='uselect',
            field=models.CharField(max_length=2, null=True, db_column=b'USELECT'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='wash',
            field=models.CharField(max_length=2, null=True, db_column=b'WASH'),
        ),
        migrations.AddField(
            model_name='newhouse',
            name='wfuel',
            field=models.CharField(max_length=2, null=True, db_column=b'WFUEL'),
        ),
    ]
