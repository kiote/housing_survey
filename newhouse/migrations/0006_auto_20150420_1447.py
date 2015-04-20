# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0005_auto_20150420_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='smsa',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'SMSA'),
        ),
    ]
