# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newhouse', '0002_auto_20150429_0529'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='newhouse',
            table='ahs_newhouse',
        ),
    ]
