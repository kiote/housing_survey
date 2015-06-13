# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homimp', '0006_auto_20150613_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homimp',
            name='rah',
            field=models.PositiveSmallIntegerField(default=None, null=True, db_column=b'RAH'),
        ),
    ]
