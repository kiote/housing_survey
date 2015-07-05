# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('year', '0002_auto_20150705_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='year',
            old_name='table_filed',
            new_name='table_field',
        ),
    ]
