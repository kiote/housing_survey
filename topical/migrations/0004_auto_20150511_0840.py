# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topical', '0003_auto_20150429_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topical',
            name='smsa',
            field=models.PositiveIntegerField(null=True, db_column=b'SMSA', db_index=True),
        ),
    ]