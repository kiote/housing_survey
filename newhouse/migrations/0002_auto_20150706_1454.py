# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='newhouse',
            index_together=set([('control', 'export_year'), ('region',), ('cmsa',), ('division',), ('metro3',)]),
        ),
    ]
