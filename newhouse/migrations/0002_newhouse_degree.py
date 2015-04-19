# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newhouse',
            name='degree',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'DEGREE'),
        ),
    ]
