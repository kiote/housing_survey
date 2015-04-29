# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repwgt', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='repwgt',
            table='ahs_repwgt',
        ),
    ]
