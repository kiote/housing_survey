# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0008_auto_20150613_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newhouse',
            name='export_year',
            field=models.PositiveSmallIntegerField(null=True, db_index=True),
        ),
        migrations.AlterIndexTogether(
            name='newhouse',
            index_together=set([('control', 'export_year'), ('field_in_2013', 'field_in_2011')]),
        ),
    ]
