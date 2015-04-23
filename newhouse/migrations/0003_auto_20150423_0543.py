# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0002_auto_20150423_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='pwt',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'PWT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='weight',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'WEIGHT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wgt90geo',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'WGT90GEO'),
        ),
    ]
