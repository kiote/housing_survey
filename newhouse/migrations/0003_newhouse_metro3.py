# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0002_newhouse_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='newhouse',
            name='metro3',
            field=models.PositiveSmallIntegerField(null=True, db_column=b'METRO3'),
        ),
    ]
