# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homimp', '0003_homimp_add_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='homimp',
            name='rahk',
            field=models.SmallIntegerField(null=True, db_column=b'RAHK'),
        ),
    ]
