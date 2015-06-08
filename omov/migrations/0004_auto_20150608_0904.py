# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omov', '0003_omov_add_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='omov',
            name='add_year',
        ),
        migrations.AddField(
            model_name='omov',
            name='export_year_2011',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='omov',
            name='export_year_2013',
            field=models.BooleanField(default=False),
        ),
    ]
