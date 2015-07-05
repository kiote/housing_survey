# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('year', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='year',
            old_name='filed',
            new_name='table_filed',
        ),
    ]
