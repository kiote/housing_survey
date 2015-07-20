# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mortg',
            name='helmp1',
            field=models.IntegerField(null=True, db_column=b'HELMP1'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='helmp2',
            field=models.IntegerField(null=True, db_column=b'HELMP2'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='helmp3',
            field=models.IntegerField(null=True, db_column=b'HELMP3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='hetyp1',
            field=models.SmallIntegerField(null=True, db_column=b'HETYP1'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='hetyp2',
            field=models.SmallIntegerField(null=True, db_column=b'HETYP2'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='hetyp3',
            field=models.SmallIntegerField(null=True, db_column=b'HETYP3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hebam3',
            field=models.IntegerField(null=True, db_column=b'HEBAM3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='hepmt3',
            field=models.IntegerField(null=True, db_column=b'HEPMT3'),
        ),
    ]
