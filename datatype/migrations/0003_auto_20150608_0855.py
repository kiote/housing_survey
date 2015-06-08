# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatype', '0002_datatype_export_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datatype',
            name='export_year',
        ),
        migrations.AddField(
            model_name='datatype',
            name='export_year_2011',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='datatype',
            name='export_year_2013',
            field=models.BooleanField(default=False),
        ),
    ]
