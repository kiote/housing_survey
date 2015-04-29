# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20150429_0523'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='person',
            table='ahs_person',
        ),
    ]
