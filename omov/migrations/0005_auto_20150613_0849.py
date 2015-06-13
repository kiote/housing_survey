# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omov', '0004_auto_20150608_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='omov',
            old_name='export_year_2011',
            new_name='field_in_2011',
        ),
        migrations.RenameField(
            model_name='omov',
            old_name='export_year_2013',
            new_name='field_in_2013',
        ),
        migrations.AddField(
            model_name='omov',
            name='export_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
