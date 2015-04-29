# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratiov', '0002_auto_20150427_0500'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ratiov',
            table='ahs_ratiov',
        ),
    ]
