# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatype', '0003_auto_20150705_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatype',
            name='table_name',
            field=models.CharField(max_length=120, db_index=True),
        ),
    ]
