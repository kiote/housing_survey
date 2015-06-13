# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homimp', '0007_auto_20150613_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homimp',
            name='rah',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'RAH'),
        ),
        migrations.AlterField(
            model_name='homimp',
            name='rahk',
            field=models.SmallIntegerField(default=None, null=True, db_column=b'RAHK'),
        ),
    ]
