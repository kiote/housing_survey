# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mortg', '0006_auto_20150606_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mortg',
            name='add_year',
        ),
        migrations.AddField(
            model_name='mortg',
            name='export_year_2011',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mortg',
            name='export_year_2013',
            field=models.BooleanField(default=False),
        ),
    ]
