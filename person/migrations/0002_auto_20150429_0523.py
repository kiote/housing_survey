# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pline',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'PLINE', db_index=True),
        ),
    ]
