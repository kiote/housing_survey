# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topical', '0004_auto_20150511_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topical',
            name='smsa',
        ),
    ]
