# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0006_auto_20150420_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='cmsa',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'CMSA'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='dish',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'DISH'),
        ),
        migrations.AlterField(
            model_name='newhouse',
            name='division',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'DIVISION'),
        ),
    ]
