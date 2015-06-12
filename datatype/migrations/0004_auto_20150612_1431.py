# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datatype', '0003_auto_20150608_0855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='datatype',
            unique_together=set([('table_name', 'field_name')]),
        ),
    ]
