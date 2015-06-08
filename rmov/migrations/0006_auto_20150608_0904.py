# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmov', '0005_rmov_add_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rmov',
            name='add_year',
        ),
        migrations.AddField(
            model_name='rmov',
            name='export_year_2011',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rmov',
            name='export_year_2013',
            field=models.BooleanField(default=False),
        ),
    ]
