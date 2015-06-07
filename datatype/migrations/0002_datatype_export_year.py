# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatype', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatype',
            name='export_year',
            field=models.PositiveSmallIntegerField(default=2013),
        ),
    ]
