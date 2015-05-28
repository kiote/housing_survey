# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0004_auto_20150511_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='smsa',
            field=models.PositiveIntegerField(null=True, db_column=b'SMSA'),
        ),
    ]
