# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortg', '0003_auto_20150511_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mortg',
            name='smsa',
        ),
        migrations.AddField(
            model_name='mortg',
            name='hebal3',
            field=models.SmallIntegerField(null=True, db_column=b'HEBAL3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='hebam3',
            field=models.SmallIntegerField(null=True, db_column=b'HEBAM3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='hecr3',
            field=models.SmallIntegerField(null=True, db_column=b'HECR3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='heinf3',
            field=models.SmallIntegerField(null=True, db_column=b'HEINF3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='heinr3',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'HEINR3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='heinw3',
            field=models.SmallIntegerField(null=True, db_column=b'HEINW3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='hepmt3',
            field=models.SmallIntegerField(null=True, db_column=b'HEPMT3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='heyrmor3',
            field=models.IntegerField(null=True, db_column=b'HEYRMOR3'),
        ),
        migrations.AddField(
            model_name='mortg',
            name='imprv3',
            field=models.SmallIntegerField(null=True, db_column=b'IMPRV3'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='amtm2',
            field=models.IntegerField(null=True, db_column=b'AMTM2'),
        ),
        migrations.AlterField(
            model_name='mortg',
            name='pmt3',
            field=models.IntegerField(null=True, db_column=b'PMT3'),
        ),
    ]
