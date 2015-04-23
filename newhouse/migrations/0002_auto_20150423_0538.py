# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0001_squashed_0008_auto_20150422_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='pwt',
            field=models.DecimalField(null=True, decimal_places=5, max_digits=10, db_column=b'PWT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='weight',
            field=models.DecimalField(null=True, decimal_places=5, max_digits=10, db_column=b'WEIGHT'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='wgt90geo',
            field=models.DecimalField(null=True, decimal_places=5, max_digits=10, db_column=b'WGT90GEO'),
        ),
    ]
