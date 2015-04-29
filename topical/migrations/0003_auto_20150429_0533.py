# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topical', '0002_auto_20150427_1535'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='topical',
            table='ahs_topical',
        ),
    ]
