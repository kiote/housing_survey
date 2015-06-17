# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omov', '0005_auto_20150613_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='omov',
            name='export_year',
            field=models.PositiveSmallIntegerField(null=True, db_index=True),
        ),
        migrations.AlterIndexTogether(
            name='omov',
            index_together=set([('control', 'export_year'), ('field_in_2013', 'field_in_2011')]),
        ),
    ]